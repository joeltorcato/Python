aluno = {
  "nome": ['joão', 'nayara', 'maria', 'ana'],
  "género": ['masculino', 'feminino', 'feminino', 'feminino'],
  "nota final": [15, 18, 20, 12]
  }

print("total de alunos: " + str(len(aluno["nome"])))
print("média da nota final: " + str(sum(aluno["nota final"]) / len(aluno["nota final"])))
print("alunos do género masculino: " + str(aluno["género"].count("masculino")))
print("alunos do género feminino: " + str(aluno["género"].count("feminino")))
print("alunos com nota final acima da média: " + str([aluno["nome"][i] for i in range(len(aluno["nota final"])) if aluno["nota final"][i] > (sum(aluno["nota final"]) / len(aluno["nota final"]))]))
print("alunos com nota final abaixo da média: " + str([aluno["nome"][i] for i in range(len(aluno["nota final"])) if aluno["nota final"][i] < (sum(aluno["nota final"]) / len(aluno["nota final"]))]))

# total de alunos: 4
# média da nota final: 16.25
# alunos do género masculino: 1
# alunos do género feminino: 3
# alunos com nota final acima da média: ['nayara', 'maria']
# alunos com nota final abaixo da média: ['joão', 'ana']
