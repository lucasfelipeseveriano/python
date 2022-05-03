
import pygame
import random

#
LARGURA = 1200
ALTURA  = 900
TELA    = (LARGURA, ALTURA)
AMARELO = (255, 255, 0)
PRETO   = (0, 0, 0)
VELOCIDADE = 5

tela = pygame.display.set_mode(TELA, 0)
pygame.display.set_caption('Game com Python')

x = LARGURA / 2
y = ALTURA / 2
raio = 30
vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:





    x += vel_x
    y += vel_y
    pygame.time.delay(10)




    if x > LARGURA + raio:
        x = -raio
    elif x + raio < 0:
        x = LARGURA + raio
    if y - raio > ALTURA:
           y  = -raio
    elif y + raio < 0:
        y = ALTURA




    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    cor = (r, g, b)

    tela.fill(PRETO)
    local = x, y
    pygame.draw.circle(tela, AMARELO, local, raio, 0)




    pygame.display.update()


    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEMOTION:
            local = evento.pos
            pass
        elif evento.type == pygame.MOUSEWHEEL:
            raio += evento.y * 5
        elif evento.type == pygame.KEYDOWN:
            if evento.unicode == '+':
                raio += 5
            elif evento.unicode == '-':
                raio -= 5
            elif evento.key == pygame.K_RIGHT:
                     vel_x = VELOCIDADE
            elif evento.key == pygame.K_LEFT:
                     vel_x = -VELOCIDADE
            elif evento.key == pygame.K_UP:
                     vel_y = -VELOCIDADE
            elif evento.key == pygame.K_DOWN:
                     vel_y = -VELOCIDADE
        elif evento.type ==  pygame.QUIT:
            exit()