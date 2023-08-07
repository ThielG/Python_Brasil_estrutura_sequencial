# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
#     (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos):

arquivo = float(input('Informe o tamanho do arquivo em MB: '))
internet = float(input('Informe a velocidade da internet em GB: '))

calculo = round(((arquivo * 8) / internet) / 60, 2)

print(f'Para baixar um arquivo de {arquivo} MB, em uma conecção de {internet} GB, '
      f'levará um total de {calculo} minutos para a finalização do download.')
