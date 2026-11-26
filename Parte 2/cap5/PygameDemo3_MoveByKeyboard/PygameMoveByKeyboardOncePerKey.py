# 1 - Importando as Bibliotecas que vamos utlizar
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path

# 2 - Criando as constantes

preto = (0, 0, 0)
dicBase = Path(__file__).resolve().parent
largura_janela = 640
altura_janela = 480
qps = 30 
bola_largura_altura = 100
maxDx = largura_janela - bola_largura_altura
maxDy = largura_janela - bola_largura_altura
alvoX = 400
alvoY = 320
alvo_largura_altura = 120
pixel_por_movimento = 3

# 3 - Inicializando o mundo

pygame.init()
janela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

# 4 - Carregando recurso: imagens, sons, etc...

bolaImagem = pygame.image.load(f'{dicBase}/imagens/bola.png')
alvoImagem = pygame.image.load(f'{dicBase}/imagens/alvo.jpg')

# 5 - Iniciando variáveis

bolaX = random.randrange(maxDx)
bolaY = random.randrange(maxDy)

alvoRect = pygame.Rect(alvoX, alvoY, alvo_largura_altura, alvo_largura_altura)

# 6 - Inicizialianado o loop

while True:
    # 7 - Dectando e verificando eventos
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                bolaX = bolaX - pixel_por_movimento
            elif evento.key == pygame.K_RIGHT:
                bolaX = bolaX + pixel_por_movimento
            elif evento.key == pygame.K_UP:
                bolaY = bolaY - pixel_por_movimento
            elif evento.key == pygame.K_DOWN:
                bolaY = bolaY + pixel_por_movimento

    # 8 - Fazendo coisas por frame
    # Verifica se a bola colidiu com o alvo
    bolaRect = pygame.Rect(bolaX, bolaY, bola_largura_altura, bola_largura_altura)
    
    if bolaRect.colliderect(alvoRect):
        print('A bola está tocando o alvo')
    
    # 9 - Limpando a Janela
    janela.fill(preto)

    # 10 - Desenhando elementos na janela

    janela.blit(bolaImagem, (bolaX, bolaY))
    janela.blit(alvoImagem, (alvoX, alvoY))

    # 11 - Atulizando a janela
    pygame.display.update()

    # 12 - Desacelerando as coisas
    clock.tick(qps)