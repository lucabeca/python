from random import randint

print("Jogo de dados:")

dado1 = randint(1, 6)
dado2 = randint(1, 6)
dado3 = randint(1, 6)
dado4 = randint(1, 6)

print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Dado 3:", dado3)
print("Dado 4:", dado4)

jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

if jogador1 > jogador2:
    print("Jogador 1 venceu!")
elif jogador2 > jogador1:
    print ("Jogador 2 venceu!")
else:
    print("Houve um empate!")