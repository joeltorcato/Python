# usei o cursor para resolver o erro de não aparecer nada no terminal

nome = "joel Pedro torcato fernandes"
nome_para_mostrar = nome.lower()

print()
print("classificador de leitura", flush=True) # flush=True serve para evitar ecrã em branco
print(
    nome_para_mostrar
    + ", o teu hobby é ler. responde à pergunta para saberes que tipo de leitor és.",
    flush=True,
)
print(flush=True)

livros_texto = input("quantos livros lês por mês, em média? ")
livros_por_mes = int(livros_texto)

print(flush=True)

if livros_por_mes < 0:
    print(
        nome_para_mostrar + ", esse número não faz sentido. corre outra vez e usa 0 ou mais.",
        flush=True,
    )
elif livros_por_mes == 0:
    print(
        nome_para_mostrar
        + ", neste momento és um leitor em pausa - há tempo para voltar às histórias.",
        flush=True,
    )
elif livros_por_mes == 1:
    print(
        nome_para_mostrar
        + ", és um leitor constante: um livro por mês já é um bom hábito.",
        flush=True,
    )
elif livros_por_mes <= 3:
    print(
        nome_para_mostrar
        + ", és um leitor dedicado - vais ao ritmo de quem gosta de mergulhar em bons livros.",
        flush=True,
    )
elif livros_por_mes <= 6:
    print(
        nome_para_mostrar
        + ", és um leitor apaixonado - praticamente um livro por semana ou mais.",
        flush=True,
    )
else:
    print(
        nome_para_mostrar
        + ", és um leitor voraz - poucos conseguem acompanhar o teu ritmo.",
        flush=True,
    )

""" d:\PIS\programação\Python\2026\May\11.05\atividades>python "classificador personalizado.py"

classificador de leitura
joel pedro torcato fernandes, o teu hobby é ler. responde à pergunta para saberes que tipo de leitor és.

quantos livros lês por mês, em média? 5 (<- resposta do utilizador)

joel pedro torcato fernandes, és um leitor apaixonado - praticamente um livro por semana ou mais. """
