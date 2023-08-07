# 10. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit:

celsius = float(input('Informe a temperatura em graus Celsius: '))

fahrenheit = (celsius * 9/5) + 32

print(f'A temperatura em graus Fahrenheit é: {round(fahrenheit, 1)} °F.')
