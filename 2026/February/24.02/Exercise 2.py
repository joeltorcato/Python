lista = []
numElementos = int(input("Digite o número de elementos da lista: "))

for i in range(numElementos):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    lista.append(elemento)

def sortList(lista: list):
    sortedList = []
    for i in range(len(lista)):
        minValue = min(lista)
        sortedList.append(minValue)
        lista.remove(minValue)
    return sortedList

print(sortList(lista))