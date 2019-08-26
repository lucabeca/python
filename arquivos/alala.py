'''Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.'''

import sys

valor_desejado = int(input("Qual valor você deseja sacar? "))

if valor_desejado > 6000:
    print("Você inseriu um valor que excede o limite.")
    sys.exit()
elif valor_desejado < 1:
    print("Você inseriu um valor abaixo do limite.")
    sys.exit()

notas_100 = valor_desejado // 100
valor_desejado %= 100
notas_50 = valor_desejado // 50
valor_desejado %= 50
notas_10 = valor_desejado // 10
valor_desejado %= 10
notas_5 = valor_desejado // 5
valor_desejado %= 5
notas_1 = valor_desejado // 1

print("\nVocê receberá:\n\n{} notas de R$100,00 \n{} notas de R$50,00 \n{} notas de R$10,00 \n{} notas de R$5,00 \n{} notas de R$1,00".format(notas_100, notas_50, notas_10, notas_5, notas_1))