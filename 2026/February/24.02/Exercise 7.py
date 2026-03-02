alunos = {
  "nome": ['joão', 'nayara', 'maria', 'ana'],
  "curso": ['PIS', 'PAV', 'PSE', 'PIS']
}

def mostraralunos(alunos: dict):
  print("total de alunos: " + str(len(alunos["nome"])))
  print ("alunos do pis: " + str(alunos["curso"].count("PIS")))
  print ("nome dos alunos de pis: " + str([alunos["nome"][i] for i in range(len(alunos["curso"])) if alunos["curso"][i] == "PIS"]))

mostraralunos(alunos)
 
 # eu não gostei do código que fiz, mas estou a usar uma forma diferente.