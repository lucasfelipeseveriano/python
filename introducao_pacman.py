#introducao_pacman



import pygame

#Constantes
LARGURA = 1024  # x
ALTURA = 767      # y
TELA = (LARGURA, ALTURA)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VELOCIDADE = 0.4
RAIO = 30


#Cria tela grafica
tela = pygame.display.set_mode(TELA, 0)
#Titulo da tela
pygame.display.set_caption('Game com Python')

x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE

#loop do jogo
while True:
    #Calcula as regras do jogo
    x += vel_x
    y += vel_y

    if x + RAIO > LARGURA:
        vel_x = -VELOCIDADE
    elif x  -  RAIO < 0:
        vel_x = VELOCIDADE
    
    if y + RAIO > ALTURA:
        vel_y  = -VELOCIDADE
    elif y  -  RAIO < 0:
        vel_y = VELOCIDADE
    
    
    local = x, y
    tela.fill(PRETO)
    #desenha um circulo preenchido
    pygame.draw.circle(tela, AMARELO, local, RAIO, 0)
    pygame.display.update()

#processa os eventos do pygame
#pega cada evento do pygame e salva na variavel "e"
    for e in pygame.event.get():
        #se o tipo de evento == SAIR ( clicou  X)
        if e.type == pygame.QUIT:
            exit() #fecha o pygame
