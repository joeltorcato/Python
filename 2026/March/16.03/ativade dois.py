import os
import re

dados = input("insira o nome de um ficheiro de texto:").strip()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, dados)

if not os.path.isfile(file_path):
    print('erro: o ficheiro não existe.')
else:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        num_linhas = len(linhas)
        num_linhas_vazias = sum(1 for linha in linhas if linha.strip() == '')
        texto = ''.join(linhas)
        num_frases = len(re.findall(r'[^.!?]*[.!?]', texto))
        num_palavras = len(re.findall(r'\b\w+\b', texto))
        print(f'número de linhas: {num_linhas}')
        print(f'número de frases: {num_frases}')
        print(f'número de linhas vazias: {num_linhas_vazias}')
        print(f'número de palavras: {num_palavras}')
    except Exception as e:
        print(f'Erro ao abrir ou ler o ficheiro: {e}')

