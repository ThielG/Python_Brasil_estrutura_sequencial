# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#     usando a seguinte fórmula:
#     (72.7*altura) - 58:

altura = float(input('Informe sua altura: '))

calculo = round((72.7 * altura) - 58, 2)

print(f'\nPara uma altura de {altura}, o peso ideal é de: {calculo}kg.')
