import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************\n")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("(1) FÁCIL | (2) MÉDIO | (3) DIFICIL")
    nivel = int(input("Escolha o nível do Jogo: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        print("NÍVEL INVÁLIDO!")


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")

        print("Você digitou: ", chute_str)

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Digite apenas numeros entre 1 e 100!\n")
            continue

        acertou =  numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!\n")
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto\n")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto\n")

            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

    print("Numero secreto: ", numero_secreto)
    print("Pontuação: {}".format(pontos))
    print("Fim de Jogo")

# Esta condição serve para importar a função e executá-la
# somente quando chamá-la, e não quando importada
if(__name__ == "__main__"):
    jogar()

#  Fim da função Jogar()
