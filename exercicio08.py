# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#    Calcule e mostre o total do seu salário no referido mês:

valor = float(input('Informe o valor que você ganha por hora: '))
horas = float(input('Informe o número de horas trabalhadas no mês: '))

salario = valor * horas

print(f'\nO total do seu salário no mês é: R$ {round(salario, 2)}.')
