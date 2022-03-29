#frutas.py


import time


#tipos de arquivos: texto ou binário
#modo de acesso ao arquivo:
# 1.Somente leitura (read) = 'r'
# 2.Escrita (write) = 'w'
# 3.Anexar (append) = 'a'



lista = []


#0
def entrar_fruta():
    fruta = input('Digite o nome de uma fruta: ')
    lista.append(fruta)

#0
def salvar_frutas():
    arquivo = open ('frutas.txt','w')
    for fruta in lista:
        arquivo.write(fruta + "\n")

    arquivo.close()
    print('Lista de frutas salva')

#0
def recuperar_frutas():
    arquivo = open ('frutas.txt','r')

    lista.clear()
    for linha in arquivo:
        vetor = linha.split('\n')
        lista.append(vetor[0])

    arquivo.close()
    print('Lista de frutas recuperada')

#0
def anexar_frutas():
    arquivo = open ('frutas.txt','r')

    for linha in arquivo:
        vetor = linha.split('\n')
        lista.append(vetor[0])

    arquivo.close()
    print('Lista de frutas anexada')

#0
def limpar_lista():
   lista.clear()
   print('Lista está vazia')



def menu():

    while True:
        print('\n\n\n##### App Frutas #####')
        print('\n\n#1 = entrar fruta')
        print('#2 = mostrar lista de frutas')
        print('#3 = salvar lista de frutas')
        print('#4 = recuperar lista de frutas')
        print('#5 = anexar lista de frutas')
        print('#6 = limpar lista de frutas')
        print('#7 = sair do programa')
        
        opcao = int(input('\nQual sua opção?'))
        if opcao == 1:
            entrar_fruta()
        elif opcao == 2:
            print(lista)
        elif opcao == 3:
            salvar_frutas()
        elif opcao == 4:
            recuperar_frutas()
        elif opcao == 5:
            anexar_frutas()
        elif opcao == 6:
            limpar_lista()
        elif opcao == 7:
            print('\nSaindo...')
            time.sleep(2)
            print('Fui!!!')
            break
        else:
            print('\n### Opção inválida!!! ###')




menu()  

