import random
import time

respostas = {
    "olá": ["Olá", "Viva!", "Como estás"],
    "bom dia": ["Bom dia", "Como posso ajudar?" ],
    "nome": ["O meu nome é Py", "Podes chamar me Py"],  
    "idade": ["Tenho 0 anos", "Vou celebrar o meu primeiro " ],
    "ajuda": ["Posso responder sobre olá, bom dia, nome, idade, ajuda, piada, adeus" ],
    "piada": ["O que disse o 0 ao 8? - Bonito cinto!"],
    "adeus": ["Adeus", "Até breve", "Tchau"],
    "horas": [time.strftime("%H:%M:%S")],
}

def obter_resposta(mensagem):
    mensagem = mensagem.lower()

    for palavra_chave, lista in respostas.items():
        if palavra_chave in mensagem:
            return random.choice(lista)
    
    return "Não entendi. Escreve 'ajuda' para ver as opções."

print("Py: Olá! Eu sou Py, um chatbot.")
print("(escreve 'sair' para terminar)")

while True:
    entrada = input("Tu: ")
    if entrada.lower() == "sair":
        print("Py: Adeus!")
        break
    resposta = obter_resposta(entrada)
    print(f"Py: {resposta}")