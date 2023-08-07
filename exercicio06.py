# 6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2

print(f"A área do círculo é: {round(area, 2)}.")
