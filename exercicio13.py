# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso
#     ideal, utilizando as seguintes fórmulas:
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7

sexo = input('Infome "H" para homem ou "M" para mulher: ').upper()
altura = float(input('Informe sua altura: '))

if sexo == 'H':
    calculo = round((72.7 * altura) - 58, 2)
elif sexo == 'M':
    calculo = round((62.1 * altura) - 44.7, 2)
else:
    print('Erro: opção inválida.')

print(f'\nPara uma altura de {altura}, o peso ideal é de: {calculo}kg.')
