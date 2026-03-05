salario = float(input("digite o salario base: "))
horaextra = int(input("digite a quantidade de horas extra que fizeste: "))
valorporhora = 20
descontos = 50
print(f"O salario é: {salario} a hora extra feita é: {horaextra} o valor por hora é: {valorporhora} os descontos são: {descontos}")

salario_total = salario + (horaextra * valorporhora) - (descontos)/100
print("O salário total é:", salario_total)