import ollama
# Define a personalidade do chatbot (system prompt)
personalidade = {
    'role': 'system',
    'content': 'És o PyBot, um assistente simpático que responde sempre em português de Portugal. Respostas curtas, no máximo 3 frases.'
}
# Histórico da conversa — começa apenas com a personalidade
historico = [personalidade.copy()]
print('=== PyBot com IA LOCAL (Ollama) ===')
print('(escreve "sair" para terminar)')
while True:
    pergunta = input('\nTu: ')
    if pergunta.lower() == 'sair':
        print('PyBot: Até à próxima!')
        break
    # Acrescentar a pergunta ao histórico
    historico.append({'role': 'user', 'content': pergunta})
    try:
        resposta = ollama.chat(model='llama3.2:1b', messages=historico)
        texto_resposta = resposta['message']['content']
        # Guardar a resposta no histórico (para o bot ter memória)
        historico.append({'role': 'assistant', 'content': texto_resposta})
        print(f'PyBot: {texto_resposta}')
    except Exception as erro:
        print(f'Erro ao contactar a IA: {erro}')
        print('Verifica se o Ollama está a correr.')