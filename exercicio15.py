# 15. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#     Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
#     o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.

horas = int(input('Informe a quantidade de horas trabalhadas: '))
valor = float(input('Informe o valor da hora: '))

bruto = valor * horas

renda = round(bruto * 0.11, 2)
inss = round(bruto * 0.08, 2)
sindicato = round(bruto * 0.05, 2)

liquido = bruto - renda - inss - sindicato

print('\n--------------------------------------')
print(f'Salário bruto: R$ {bruto}.')
print('--------------------------------------')
print(f'Descontos:')
print(f'  - IR (11%): R$ {renda}. \n  - INSS (8%): R$ {inss}. \n  - Sindicato (5%): R$ {sindicato}.')
print('--------------------------------------')
print(f'Salário líquido: R$ {liquido}')
print('--------------------------------------')
