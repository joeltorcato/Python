list = ["ligou para a vítima?", "esteve no local do crime?", "mora perto da vítima?", "tinha algum conflito com a vítima?", 
        "já trabalhou com a vítima?"]

resposta = 0
for i in list:
    resposta = input(i + " (s/n) ")
    if resposta == "s":
        resposta += 1

if resposta == 2:
    print("suspeito")
elif resposta >= 2 and resposta <= 3:
    print("cúmplice")
elif resposta == 5:
    print("assassino")
else:
    print("inocente")

# não tenho o que comentar