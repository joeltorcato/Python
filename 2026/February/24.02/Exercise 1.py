#o utilizador nao faz nada
notas = [20,19,20,19,20,18]

def maxLista(lista: list):
    while len(lista) == 0:
        return 0
    maxValue = max(lista)
    return maxValue

def maxLista2(lista: list):
    for i in range(1):
        if len(lista) == 0:
            return 0
        maxValue = max(lista)
        return maxValue


print(maxLista(notas))
print(maxLista2(notas))