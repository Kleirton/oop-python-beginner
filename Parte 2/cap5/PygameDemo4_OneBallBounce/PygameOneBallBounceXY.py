# 1 - Importando os Pacotes

import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

# 2 - Definindo as constantes

preto = (0, 0, 0)
dirBase = Path(__file__).resolve().parent
janela_altura = 480
janela_largura = 640
qps = 60
bola_largura_altura = 100
maxDx = janela_largura - bola_largura_altura
maxDy = janela_altura - bola_largura_altura
velocidade_pixel_por_quadro = 3

# 3 - Inicilizando o mundo

pygame.init()
janela = pygame.display.set_mode((janela_largura, janela_altura))
clock = pygame.time.Clock()

# 4 - Carregando os assets (recursos)

imagemBola = pygame.image.load(f'{dirBase}/imagens/bola.png')

# 5 - Inicinado as variáveis

bolaX = random.randrange(maxDx)
bolaY = random.randrange(maxDy)
xVel = velocidade_pixel_por_quadro
yVel = velocidade_pixel_por_quadro

# 6 - Loop infinito

while True:
    # 7 - Verificando eventos
    for evento in pygame.event.get():
        # Verificando evento de fechar janela
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo coisas por frame

    if (bolaX < 0) or (bolaX >= maxDx):
        # invertendo a velocidade
        xVel = -xVel
    if (bolaY < 0) or (bolaY >= maxDy):
        # invertendo a velocidade
        yVel = -yVel
    
    #Atulizando a localização da bola, usando a velocidade nas duas direções
    bolaX += xVel
    bolaY += yVel

    # 9 - Preenchendo a janela

    janela.fill(preto)

    # 10 - desenhando elementos na janela

    janela.blit(imagemBola, (bolaX, bolaY))

    # 11 - Atulizand a janela

    pygame.display.update()

    # 12 - desacelerando as coisas

    clock.tick(qps)