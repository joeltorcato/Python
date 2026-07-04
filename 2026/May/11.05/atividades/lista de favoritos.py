# este exercício estava um pouco confuso, para ser sincero

cidade = "loures"
hobby = "ler"

favoritos = ["fantasia", "ficção científica", "história", "biografias", "bandas desenhadas"]

print("sou de " + cidade + " e adoro " + hobby + ". estas são coisas que gosto de ler:")
for coisa in favoritos:
    print("  - " + coisa)

favoritos.append("poesia") # adicionei poesia (MELHOR ESTILO, OBRIGADO FERNANDO PESSOA)
favoritos.remove("ficção científica") # nem preciso dizer o que fiz aqui
favoritos.sort()

print()
print("atualizei a lista: acrescentei poesia, tirei ficção científica e ordenei alfabeticamente.")
print("em " + cidade + " leio de tudo, mas isto é o que ficou na lista agora:")
for coisa in favoritos:
    print("  - " + coisa)

""" d:\PIS\programação\Python\2026\May\11.05\atividades>python "d:\PIS\programação\Python\2026\May\11.05\atividades\lista de favoritos.py"
sou de loures e adoro ler. estas são coisas que gosto de ler:
  - fantasia
  - ficção científica
  - história
  - biografias
  - bandas desenhadas

atualizei a lista: acrescentei poesia, tirei ficção científica e ordenei alfabeticamente.
em loures leio de tudo, mas isto é o que ficou na lista agora:
  - bandas desenhadas
  - biografias
  - fantasia
  - história
  - poesia """