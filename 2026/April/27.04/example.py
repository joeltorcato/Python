from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

dados = [
    [30, 40, 0],
    [25, 60, 0],
    [50,10,0],
    [20,0,0],
    [90,20,1],
    [20,10,1],
    [220,0,1],
    [22,10,1],
    [10,300,1],
    [10,201,1]
]

x = [[d[0], d[1]] for d in dados]
y = [d[2] for d in dados]

arvore = DecisionTreeClassifier(max_depth=3)
arvore.fit(x, y)

regras = export_text(arvore, feature_names=['temperatura', 'humidade'])
print("regras da arvore: ")
print(regras)

temp = float(input("Temperatura: (ºC): "))
hum = float(input("Humidade: (%): "))
previsao = arvore.predict([[temp, hum]])
print("previsão: CHOVEEE!!" if previsao[0] == 1 else "previsão: NÃO CHOVE!!")