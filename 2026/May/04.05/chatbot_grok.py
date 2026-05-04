import requests

chave_api = "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"
url = "https://api.groq.com/openai/v1/chat/completions"
model = "llama-3.3-70b-versatile"

personalidade = {
    "role": "system",
    "content": "És um assistente de IA chamado Py. Responde em portugues de Portugal. respostas curtas, no máximo 3 frases",
}

historico = [personalidade]

def perguntar_ia(historico_completo):

    cabecalho = {
        "Authorization": f"Bearer {chave_api}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": historico_completo,
        "max_tokens": 300
    }
    resposta = requests.post(url, headers=cabecalho, json=payload)
    resposta.raise_for_status()
    resposta_json = resposta.json()
    texto = resposta_json["choices"][0]["message"]["content"].strip()
    return texto

print("Py: Olá! Eu sou Py, um chatbot.")
print("(escreve 'sair' para terminar)")

while True:
    entrada = input("Tu: ")
    if entrada.lower() == "sair":
        print("Py: Adeus!")
        break
    historico.append({"role": "user", "content": entrada})
    resposta = perguntar_ia(historico)
    print(f"Py: {resposta}")
    historico.append({"role": "assistant", "content": resposta})
