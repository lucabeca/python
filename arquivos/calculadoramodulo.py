input_string = input("Insira os valores que você deseja calcular, separando os por vírgulas: ")

list = input_string.split(',')

positivos = []

for n in list:
    n = int(n)
    if n < 0:
        print(n * -1)
    else:
        print(n)