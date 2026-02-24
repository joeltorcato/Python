dados = input("escreve números inteiros:")
lista = [int(x) for x in dados.split()]

def medialista(lista):
    media = sum(lista) / len(lista)
    print(media)

medialista(lista) # a média