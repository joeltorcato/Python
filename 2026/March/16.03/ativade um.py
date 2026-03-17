import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'atividade13.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

palavra = input('palavra a procurar: ')
encontradas = []

for i, linha in enumerate(linhas, 1):
    if palavra in linha:
        encontradas.append(f"linha {i}: {linha.strip()}")

if encontradas:
    print('\n'.join(encontradas))
else:
    print('a palavra não foi encontrada no ficheiro.')