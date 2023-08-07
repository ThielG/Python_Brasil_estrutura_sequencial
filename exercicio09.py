# 9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
#    em graus Celsius:

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

celsius = (fahrenheit - 32) * 5/9

print(f'A temperatura em graus Celsius é: {round(celsius)} °C.')
