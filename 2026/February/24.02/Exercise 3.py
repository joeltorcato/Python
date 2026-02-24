list = [1, 2, 3, 4, 5]

if (repetidos := set([x for x in list if list.count(x) > 1])):
    print(repetidos)
else:
    print("não tem elementos repetidos") # neste caso esta será a resposta