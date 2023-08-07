# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
#     área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
#     que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que
#     custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
#     e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))

quantidade = area * 1 / 6 * 1.1

lata = math.ceil(quantidade / 18)
galao = math.ceil(quantidade / 3.6)

preco_lata = round(lata * 80.00, 2)
preco_galao = round(galao * 25.00, 2)

latas = math.ceil(quantidade / 18)
sobra = (latas * 18) - quantidade
galoes = math.ceil(sobra / 3.6)

preco = round((latas * 80.00) + (galoes * 25.00), 2)

print(f'\nQuantidade de latas de tinta a serem compradas: {lata} latas. \nPreço: R$ {preco_lata}.')
print(f'\nQuantidade de galões de tinta a serem compradas: {galao} galões. \nPreco: R$ {preco_galao}.')
print(f'\nQuantidade de latas e galões a serem compradas: {latas} latas e {galoes} galões. \nPreço: R% {preco}.')
