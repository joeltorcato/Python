from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

print('dados carregados com sucesso:', iris.target_names)
print('forma dos dados:', X.shape)

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_treino, y_treino)

previsoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)
print(f'acurácia do modelo: {acuracia * 100:.2f}%')

nova_flor = [[5.1, 3.5, 1.4, 0.2]]
resultado = modelo.predict(nova_flor)
print(f'previsão para nova flor: {iris.target_names[resultado][0]}')
