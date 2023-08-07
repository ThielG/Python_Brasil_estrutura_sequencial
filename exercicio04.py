# 4. Faça um programa que peça as 4 notas bimestrais e mostre a média:

primeira = float(input('Informe a primeira nota: '))
segunda = float(input('Informe a segunda nota: '))
terceira = float(input('Informe a terceira nota: '))
quarta = float(input('Informe a quarta nota: '))

notas = [primeira, segunda, terceira, quarta]
media = (sum(notas) / 4)

print('\nAvaliação | Nota')
print('----------------')

for i in range(len(notas)):
    print(f'{(i + 1):8}° | {notas[i]:4}')

print('----------------')
print(f'Média:      {round(media, 2)}')
print('----------------')
