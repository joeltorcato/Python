import ollama

# Personalidade: chef de cozinha entusiasta de receitas tradicionais portuguesas
personalidade = {
    'role': 'system',
    'content': 'És um chef de cozinha entusiasta que só fala sobre receitas tradicionais portuguesas. Responde sempre em português de Portugal. Respostas curtas, no máximo 3 frases.'
}
historico = [personalidade.copy()]

print('=== PyBot com IA LOCAL (Ollama) ===')
print('(escreve "sair" para terminar, "limpar" para esquecer a conversa, "guardar" para gravar o histórico)')

def guardar_historico(historico):
    with open("conversa_ia.txt", "w", encoding="utf-8") as f:
        for msg in historico:
            f.write(f"{msg['role']}: {msg['content']}\n")
    print("Histórico guardado em conversa_ia.txt.")

while True:
    pergunta = input('\nTu: ')
    if pergunta.lower() == 'sair':
        print('PyBot: Até à próxima! Bom apetite!')
        break
    elif pergunta.lower() == 'limpar':
        historico = [personalidade.copy()]
        print("PyBot: Esqueci a conversa. Pronto para novas receitas!")
        continue
    elif pergunta.lower() == 'guardar':
        guardar_historico(historico)
        continue
    historico.append({'role': 'user', 'content': pergunta})
    try:
        resposta = ollama.chat(model='llama3.2:1b', messages=historico)
        texto_resposta = resposta['message']['content']
        historico.append({'role': 'assistant', 'content': texto_resposta})
        print(f'PyBot: {texto_resposta}')
    except Exception as erro:
        print(f'Erro ao contactar a IA: {erro}')
        print('Verifica se o Ollama está a correr.')