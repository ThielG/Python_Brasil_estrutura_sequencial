# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#     a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
#     é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
#     a serem compradas e o preço total:

import math

area = float(input('Informe o tamanho da área a ser pintada (em metros quadrados): '))

litros = area / 3

quantidade = math.ceil(litros / 18)

preco = 80.00
total = round(quantidade * preco, 2)

print(f'\nQuantidade de latas de tinta a serem compradas: {quantidade}. \nPreço total: R$ {total}')
