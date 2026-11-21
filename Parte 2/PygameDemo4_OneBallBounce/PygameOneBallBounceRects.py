# 1 - Importando as bibliotecas

import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

# 2 - Definindo as constantes

preto = (0, 0, 0)
janela_largura = 640
janela_altura = 480
qps = 60
dirBase = Path(__file__).resolve().parent
pixelPorSeg = 3

# 3 - Inicializnado o ambiente

pygame.init()
janela = pygame.display.set_mode((janela_largura, janela_altura))
clock = pygame.time.Clock()

# 4 - Carregando os recursos (assests)

bolaImagem = pygame.image.load(f'{dirBase}/imagens/bola.png')

# 5 - Inicilizando variáveis

bolaRect = bolaImagem.get_rect()
maxDx = janela_largura - bolaRect.width
maxDy = janela_altura - bolaRect.height
bolaRect.x = random.randrange(maxDx)
bolaRect.y = random.randrange(maxDy)
xVel = pixelPorSeg
yVel = pixelPorSeg

# 6 - Loop princpal

while True:
    
    # 7 - Verificando por eventos

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo coisas por quadro

    if (bolaRect.x < 0) or (bolaRect.x >= maxDx):
        xVel = -xVel
    
    if (bolaRect.y < 0) or (bolaRect.y >= maxDy):
        yVel = -yVel
    
    bolaRect.x = bolaRect.x + xVel
    bolaRect.y = bolaRect.y + yVel

    # 9 - Limpando a tela

    janela.fill(preto)

    # 10 - Coisas na tela

    janela.blit(bolaImagem, bolaRect)

    # 11 - Atulziando a janela

    pygame.display.update()

    # 12 - Desacelerando as coisas

    clock.tick(qps)