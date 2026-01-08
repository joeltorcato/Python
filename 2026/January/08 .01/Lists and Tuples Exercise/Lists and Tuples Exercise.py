
notas = [14, 12, 16, 10, 18] 
print("Lista completa de notas:", notas)
print("Número total de notas:", len(notas))
print("Nota mais alta:", max(notas))
print("Nota mais baixa:", min(notas))
print("Média das notas:", sum(notas) / len(notas))

nova_nota = int(input("Insira uma nova nota: "))
notas.append(nova_nota)
print("Lista de notas após adicionar nova nota:", notas)

notas.sort()
print("Lista ordenada por ordem crescente:", notas)

notas = [nota for nota in notas if nota >= 10]
print("Lista após remover notas inferiores a 10:", notas)

disciplinas = ("Programação", "Redes", "Sistemas Operativos", "Multimédia")
print("\nTodas as disciplinas:", disciplinas)
print("Primeira disciplina:", disciplinas[0])
print("Última disciplina:", disciplinas[-1])
print("Número de disciplinas:", len(disciplinas))
aluno = input("Insira o nome do aluno: ")
print("Nome do aluno:", aluno)

disciplina_check = "Programação"
if disciplina_check in disciplinas:
    print(f'A disciplina "{disciplina_check}" existe na tupla.')
else:
    print(f'A disciplina "{disciplina_check}" não existe na tupla.')

disciplinas_praticadas = [] 
for disciplina in disciplinas:
    if len(disciplina) > 8:
        disciplinas_praticadas.append(disciplina)
print("\nDisciplinas praticadas (nome > 8 caracteres):", disciplinas_praticadas)

disciplinas_praticadas_tuple = tuple(disciplinas_praticadas)
print("Disciplinas praticadas como tupla:", disciplinas_praticadas_tuple)

# joel, não gosto de comentar.



