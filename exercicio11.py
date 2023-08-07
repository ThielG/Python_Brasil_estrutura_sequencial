# 11. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     A) o produto do dobro do primeiro com metade do segundo .
#     B) a soma do triplo do primeiro com o terceiro.
#     C) o terceiro elevado ao cubo.

primeira = int(input('Informe o primeiro número inteiro: '))
segunda = int(input('Informe o segundo número inteiro: '))
terceiro = float(input('Agora informe um número real: '))

dobro = (2 * primeira) * (segunda / 2)
triplo = (3 * primeira) + terceiro
cubo = terceiro ** 3

print(f'\nO produto do dobro de {primeira} com metade de {segunda} é: {dobro}.\nA soma do triplo de {primeira} com '
      f'metade de {segunda} é: {triplo}. \nE, {terceiro} elevado ao cubo é: {triplo}.')
