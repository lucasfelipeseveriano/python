#jogo_da_forca.py

palavra_secreta = "BARATO"
tamanho = len(palavra_secreta)#6
acertos = 0
ja_foi = []
partes_corpo = ["cabeça","tronco","perna esquerda","perna direita","braço direito","braço esquerdo"]
digitadas = []


def mostrar_digitadas():
    print('Palavra secreta:', end='')
    for item in digitadas:
        print(item, end=' ')
        
def salvar_letra(letra):
    ind = 0
    encontrou = 0
    for c in palavra_secreta:
        if c == letra:
            encontrou +=1
            digitadas[ind] = letra
        ind +=1
    return encontrou



print('\n\n\t\t############################')
print('\t\t#Bem vindo ao jogo da forca#')
print('\t\t############################')


for letra in palavra_secreta:
    print("__",end='  ')
    digitadas.append('__')
print()


while True:
    letra = input('\nDigite uma letra:').upper()

    if len(letra) == 0:
        continue

    if letra in ja_foi:
        print('\nJá foi digitada! Tentar outra!')
        continue

    if letra in palavra_secreta:
        print('\nAcertou. Muito bem!')
        acertos +=salvar_letra(letra)
        mostrar_digitadas()

        if acertos == tamanho:
            print('\nVocê venceu! Parabéns!!!')
            break

    else:
        print('Errou! HEHEHE. Enforcou:',partes_corpo[0])
        del partes_corpo[0]
        if len(partes_corpo)== 0:
            print('\nVocê perdeu! HAHAHAHA')
            break


    
