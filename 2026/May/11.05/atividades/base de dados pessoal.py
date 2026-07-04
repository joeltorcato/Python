perfil = {
    "nome": "joel pedro torcato fernandes",
    "idade": 17,
    "cidade": "loures",
    "hobby": "ler",
    "animal": "cão",
    "comida_favorita": "língua de vaca",
    "serie_favorita": "friends", # MELHOR SERIE DE TODOS OS TEMPOS (o professor concorda comigo) 
}

print("resumo das chaves do perfil")
print(list(perfil.keys())) # lista de chaves do perfil, eu vi aqui: https://www.geeksforgeeks.org/python/python-print-dictionary-keys-and-values/
print()

print("resumo dos valores")
print(list(perfil.values()))
print()

print("perfil formatado (campo a campo)")
for campo, valor in perfil.items():
    print("  " + str(campo).ljust(18) + ": " + str(valor)) # ljust(18) serve para alinhar o texto à esquerda e preencher com espaços para que o texto fique com 18 caracteres de largura, não sabia que existia mas achei útil
print()

# get() com chave que existe
print("idade registada:", perfil.get("idade"))
# get() com chave que não existe (default útil para dados opcionais)
print("telefone:", perfil.get("telefone", "não está guardado no dicionário"))
print() 
# como era preciso usar, fiz dessa forma

""" d:\PIS\programação\Python\2026\May\11.05\atividades>python "d:\PIS\programação\Python\2026\May\11.05\atividades\base de dados pessoal.py"
resumo das chaves do perfil
['nome', 'idade', 'cidade', 'hobby', 'animal', 'comida_favorita', 'serie_favorita']

resumo dos valores
['joel pedro torcato fernandes', 17, 'loures', 'ler', 'cão', 'língua de vaca', 'friends']

perfil formatado (campo a campo)
  nome              : joel pedro torcato fernandes
  idade             : 17
  cidade            : loures
  hobby             : ler
  animal            : cão
  comida_favorita   : língua de vaca
  serie_favorita    : friends

idade registada: 17
telefone: não está guardado no dicionário """