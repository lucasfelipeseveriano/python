#Adivinhacao.py


import random

total_de_tentativas=5
pontos=1000


print("Qual o nivel de dificuldade?")
print("(1)Facil (2)Medio (3)Dificil")

nivel=int(input("Defina o nivel:"))

if(nivel==1):
    total_de_tentativas=15
elif(nivel==2):
    total_de_tentativas=10
else:
    total_de_tentativas=5


numero_secreto=random.randrange(1,101)


for tentativa in range(1,total_de_tentativas+1):

    print("tentativa {} de {}".format(tentativa,total_de_tentativas))
    
    str_chute=input("Digite um numero entre 1 e 100:")
    chute=int(str_chute)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um  numero entr 1 e 100")
        continue

    if chute==numero_secreto:
        print("acertou")
        break
    else:
        
        pontos_perdidos=abs(numero_secreto - chute)
        pontos=pontos - pontos_perdidos

        if chute > numero_secreto:
           print("Errou! seu chute foi maior que o numero secreto")
        else:
            print("Errou! seu chute foi menor que o numero secreto")

print("Fim do jogo")
print("O numero secreto era {}. Voce fez {}".format(numero_secreto,pontos))
