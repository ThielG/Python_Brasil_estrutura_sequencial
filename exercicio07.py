# 7. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário:

lado = float(input('Informe o valor de um lado do quadrado (em metros): '))

area = lado * lado
dobro = area * 2

print(f'\nA área do quadrado é: {area}m².')
print(f'O dobro da área do quadrado é: {dobro}m².')
