#introducao_pygame.py

#pip install pygame

import pygame
import math


#Constantes gerais
#
VERMELHO = (255, 0, 0)
VERDE    = (0, 255, 0)
AZUL     = (0, 0, 255)
PRETO    = (0, 0, 0)
BRANCO   = (255, 255, 255)
AMARELO  = (255, 255, 0)
LARANJA  = (255, 165, 0)
PI = math.pi

pygame.init()


tela = pygame.display.set_mode((640, 480), 0)
pygame.display.set_caption('Titulo da janela')


#pinta tela
tela.fill(LARANJA)


pygame.draw.circle(tela, BRANCO,(50, 50), 10, 10)
pygame.draw.circle(tela, BRANCO,(100, 50), 15, 1)
pygame.draw.circle(tela, BRANCO,(150, 50), 20, 5)

pygame.draw.rect(tela, PRETO, pygame.Rect(200, 30, 60, 30), 0)
pygame.draw.rect(tela, AZUL, pygame.Rect(280, 30, 60, 30), 1)

pygame.draw.line(tela, VERMELHO,[450,20],[550,130],5)

pontos = [(50, 150), (100, 120), (160,140), (110,250)]
pygame.draw.polygon(tela, AMARELO, pontos, 0)
pygame.draw.polygon(tela, AZUL, pontos, 2)


pygame.draw.arc(tela, VERMELHO, [250, 100, 250, 200],PI/2, PI, 5)
pygame.draw.arc(tela, VERMELHO, [250, 100, 250, 200],    0, PI/2, 5)
pygame.draw.arc(tela, VERMELHO, [250, 100, 250, 200],3*PI/2, 2/PI, 5)
pygame.draw.arc(tela, VERMELHO, [250, 100, 250, 200],       PI, 3*PI/2, 5)



texto = "Score:{}".format(1000)
fonte = pygame.font.SysFont("arial", 48, True, False)
img_texto = fonte.render(texto, True, VERDE)
tela.blit(img_texto, (50, 350))



pygame.display.update()
