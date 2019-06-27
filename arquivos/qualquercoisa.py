import time
print("Calculadora de punhetas")

idade = int(input("Digite a sua idade: "))
media = int(input("Digite a sua média por semana estimada: "))

dias = (idade - 11) * (53 * media)
total = dias - (idade - 11 * (3 * media))
total = round(total, 0)

print('Você já bateu, aproximadamente, algo entre',total - (53 * media),'e', total, 'punhetas.')