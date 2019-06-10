from random import randint
import time

print("Super calculadora do amor")

nome1 = input("Digite o nome da primeira pessoa: ")
nome2 = input("Digite o nome da segunda pessoa: ")
resultado = randint(0,100)

print("Consultando cupido...")
time.sleep(1)
print("Consultando estrelas...")
time.sleep(1)
print("Consultando planetas...")
time.sleep(1)

if resultado <= 50:
    print("O resultado foi:", resultado, "%")
    print("Que triste! O amor não está no ar.")
elif resultado <= 75:
    print("O resultado foi:", resultado, "%")
    print("Que maravilha! O amor está no ar.")
else:
    print("O resultado foi:", resultado, "%")
    print("Its a match!", nome1, "love", nome2)