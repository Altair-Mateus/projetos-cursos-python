import adivinhacao
import forca

print("*********************************")
print("********Escolha um Game!*********")
print("*********************************")

print("(1) Forca | (2) Adivinhação")

jogo = int(input("Jogo Escolhido: "))


if(jogo == 1):

    print("Iniciando jogo da forca...\n")
    forca.jogar()

elif(jogo == 2):

    print("Iniciando jogo de adivinhação...\n")
    adivinhacao.jogar()

else:
    print("Código de game inválido!")

# Fim do bloco if-else