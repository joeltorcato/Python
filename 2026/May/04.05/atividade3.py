import json
import os
import re
import sys
from pathlib import Path

import requests

url = "https://api.groq.com/openai/v1/chat/completions"
model = "llama-3.3-70b-versatile"

# Caso de uso real: tutor de apoio ao estudo de Python (aula PIS / trabalhos de casa).
personalidade = {
    "role": "system",
    "content": (
        "És o Py, um tutor de apoio em Python para alunos (disciplina PIS ou equivalente). "
        "O utilizador conversa contigo como faria com um colega mais experiente: "
        "explica erros de código e mensagens do interpretador, ajuda a perceber enunciados, "
        "sugere passos ou correcções pontuais, e esclarece conceitos (listas, ciclos, funções, ficheiros, etc.). "
        "Não entregues soluções completas copiáveis quando o enunciado exige trabalho individual; "
        "orienta para o aluno chegar lá. "
        "Responde sempre em português de Portugal, com tom claro e pedagógico. "
        "Por omissão, no máximo 3 frases; se pedirem mais pormenor, podes alongar um pouco."
    ),
}


def _raiz_repositorio():
    return Path(__file__).resolve().parents[3]


def obter_chave_api():
    env = os.environ.get("GROQ_API_KEY", "").strip()
    if env:
        return env
    raiz_repo = _raiz_repositorio()
    for candidato in (Path(__file__).resolve().parent / "chave.txt", raiz_repo / "chave.txt"):
        if not candidato.is_file():
            continue
        texto = candidato.read_text(encoding="utf-8").strip()
        m = re.search(r"=\s*(\S+)", texto)
        if m:
            return m.group(1).strip()
        if texto and not texto.startswith("#"):
            return texto
    print(
        "Erro: não encontrei chave da API. Define GROQ_API_KEY ou cria chave.txt com a chave.",
        file=sys.stderr,
    )
    sys.exit(1)


chave_api = obter_chave_api()


def perguntar_ia(historico_completo):
    cabecalho = {
        "Authorization": f"Bearer {chave_api}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": historico_completo,
        "max_tokens": 300,
    }
    resposta = requests.post(url, headers=cabecalho, json=payload, timeout=60)
    resposta.raise_for_status()
    resposta_json = resposta.json()
    return resposta_json["choices"][0]["message"]["content"].strip()


def historico_valido(dados):
    if not isinstance(dados, list) or not dados:
        return False
    for msg in dados:
        if not isinstance(msg, dict):
            return False
        if msg.get("role") not in ("system", "user", "assistant"):
            return False
        if "content" not in msg or not isinstance(msg["content"], str):
            return False
    return dados[0].get("role") == "system"


def _candidatos_caminho(relative: str):
    """Ordem: pasta atual (onde correu o python), pasta do script, raiz do repo."""
    p = Path(relative)
    yield p
    if not p.is_absolute():
        yield Path(__file__).resolve().parent / relative
        yield _raiz_repositorio() / relative


def _primeiro_ficheiro_existente(relative: str):
    for candidato in _candidatos_caminho(relative):
        if candidato.is_file():
            return candidato
    return None


def guardar_conversa(caminho, historico):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)
    print(f"Py: Conversa guardada em «{caminho.resolve()}».")


def carregar_conversa(relative: str):
    caminho = _primeiro_ficheiro_existente(relative)
    if caminho is None:
        procurados = [str(c.resolve()) for c in _candidatos_caminho(relative)]
        print("Py: Ficheiro não encontrado com esse nome.")
        print(
            "Py: Usa o mesmo nome que em «guardar como», ou o caminho completo. "
            "(«ficheiro.json» nos exemplos é só um placeholder.)"
        )
        print("Py: Procurei em:")
        for linha in procurados:
            print(f"    - {linha}")
        return None
    resolvido = caminho.resolve()
    try:
        texto = caminho.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Py: Não consegui abrir «{resolvido}» ({e}).")
        return None
    if not texto.strip():
        print(f"Py: O ficheiro «{resolvido}» está vazio.")
        print(
            "Py: Apaga-o ou grava uma conversa com «guardar como ...» a partir deste programa "
            "(não deixes o ficheiro aberto no editor sem conteúdo JSON)."
        )
        return None
    try:
        dados = json.loads(texto)
    except json.JSONDecodeError as e:
        print(f"Py: O ficheiro «{resolvido}» não tem JSON válido ({e}).")
        print(
            "Py: O formato correcto é o que «guardar como» gera (lista de mensagens). "
            "Corrige o ficheiro ou guarda de novo a partir de uma conversa."
        )
        return None
    if not historico_valido(dados):
        print(
            "Py: O ficheiro não parece uma conversa deste programa "
            "(é preciso uma lista de mensagens e a primeira com role «system»)."
        )
        return None
    return dados


def _despedida(pedidos_api: int) -> None:
    print(f"\nPedidos à API nesta sessão: {pedidos_api}")
    if pedidos_api > 50:
        print(
            "\nAviso: foram feitos mais de 50 pedidos à API nesta sessão. "
            "Usa a conversa com critério para não gastar a chave partilhada desnecessariamente."
        )


def main():
    historico = [dict(personalidade)]
    pedidos_api = 0

    print("=== Py — tutor de Python (caso de uso: estudo e exercícios) ===")
    print(
        "Py: Olá! Escreve em texto livre — cada mensagem que não for comando é enviada à IA "
        "e eu respondo como tutor (erros, dúvidas, código, conceitos)."
    )
    print("Exemplos: «Porque é que dá NameError aqui?» ou «Explica-me o que faz o for».")
    print(
        "Comandos: «sair» | «guardar como <nome>.json» | «carregar <nome>.json» | «ajuda» "
        "(substitui <nome> pelo ficheiro que criaste com «guardar como».)"
    )
    print("(Podes guardar a conversa e continuar noutro dia com «carregar».)")
    print("Py: (Ctrl+C também termina e mostra o contador de pedidos.)")

    try:
        while True:
            try:
                entrada = input("Tu: ").strip()
            except EOFError:
                print("\nPy: Fim da entrada (EOF). Até logo!")
                _despedida(pedidos_api)
                break
            if not entrada:
                continue

            lower = entrada.lower()
            if lower == "sair":
                print("Py: Adeus!")
                _despedida(pedidos_api)
                break

            if lower == "ajuda":
                print(
                    "Py: Sou um tutor de Python: pergunta o que quiseres sobre código ou teoria — "
                    "isso vai para a IA e recebes resposta. "
                    "«guardar como caminho/conversa.json» grava o histórico (JSON válido). "
                    "«carregar caminho/conversa.json» retoma uma sessão (o ficheiro não pode estar vazio). "
                    "«sair» ou Ctrl+C terminam e mostram quantos pedidos fizeste à API."
                )
                continue

            if lower.startswith("guardar como"):
                resto = entrada[len("guardar como") :].strip()
                if not resto:
                    print("Py: Indica o ficheiro, por exemplo: guardar como minha_conversa.json")
                    continue
                guardar_conversa(resto, historico)
                continue

            if lower.startswith("carregar"):
                resto = entrada[len("carregar") :].strip()
                if not resto:
                    print("Py: Indica o ficheiro, por exemplo: carregar minha_conversa.json")
                    continue
                novo = carregar_conversa(resto)
                if novo is not None:
                    historico = novo
                    print(f"Py: Conversa carregada ({len(historico) - 1} mensagens após o sistema).")
                continue

            historico.append({"role": "user", "content": entrada})
            try:
                resposta = perguntar_ia(historico)
            except requests.HTTPError as e:
                historico.pop()
                print(f"Py: Erro ao contactar a API ({e}). Tenta de novo mais tarde.")
                continue
            except requests.RequestException as e:
                historico.pop()
                print(f"Py: Problema de rede ou tempo esgotado ({e}).")
                continue

            pedidos_api += 1
            print(f"Py: {resposta}")
            historico.append({"role": "assistant", "content": resposta})
    except KeyboardInterrupt:
        print("\nPy: Interrompido (Ctrl+C). Até logo!")
        _despedida(pedidos_api)


if __name__ == "__main__":
    main()
