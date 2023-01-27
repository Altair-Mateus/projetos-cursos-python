import random


print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Digite apenas numeros entre 1 e 100!")
        continue

    acertou =  numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

print("Numero secreto: ", numero_secreto)
print("Fim de Jogo")


