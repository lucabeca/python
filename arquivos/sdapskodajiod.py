'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

valor1 = input("Insira o valor 1: ")
valor2 = input("Insira o valor 2: ")
operacao = input("Qual operação você deseja realizar? ")

if operacao == '*':
    resultado = valor1 * valor2
    print("O resultado da operação é", resultado)
    if resultado % 2 == 0:
        print("O valor é par")
    if resultado < 0:
        print("O resultado é negativo")
    else:
        print("O resultado é positivo")
elif operacao == '/':
    resultado = valor1 / valor2
    print("O resultado da operação é", resultado)
    if resultado % 2 == 0:
        print("O valor é par")
    if resultado < 0:
        print("O resultado é negativo")
    else:
        print("O resultado é positivo")
elif operacao == '+':
    resultado = valor1 + valor2
    print("O resultado da operação é", resultado)
    if resultado % 2 == 0:
        print("O valor é par")
    if resultado < 0:
        print("O resultado é negativo")
    else:
        print("O resultado é positivo")
elif operacao == '-':
    resultado = valor1 - valor2
    print("O resultado da operação é", resultado)
    if resultado % 2 == 0:
        print("O valor é par")
    if resultado < 0:
        print("O resultado é negativo")
    else:
        print("O resultado é positivo")