print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 10

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou ebaa!")
else:
    print("Você errou hein!")

print("Game over")