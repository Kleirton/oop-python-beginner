# 1 - Importando as coisas
import pygame
from pygame.locals import * 
from pathlib import Path
import sys
import random

# 2 - Definindo as variáveis

preto = (0, 0, 0)
janela_altura = 480
janela_largura = 640
qps = 60
dirBase = Path(__file__).resolve().parent
pps = 3

# 3 - Inicinado o ambiente

pygame.init()
janela = pygame.display.set_mode((janela_largura, janela_altura))
clock = pygame.time.Clock()

# 4 - Carregando recuros (assets)

imagemBola = pygame.image.load(f'{dirBase}/imagens/bola.png')
boingSom = pygame.mixer.Sound(f'{dirBase}/sons/boing.wav')
pygame.mixer.music.load(f'{dirBase}/sons/background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Carregando variáveis

bolaRect = imagemBola.get_rect()
maxDx = janela_largura - bolaRect.width
maxDy = janela_altura - bolaRect.height
bolaRect.x = random.randrange(maxDx)
bolaRect.y = random.randrange(maxDy)
xVel = pps
yVel = pps

# 6 - Loop principal

while True:
    # 7 - Dectetando eventos

    for evento in pygame.event.get():
        # Dectatndo evento de fechar a janela
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo coisas por frame

    if (bolaRect.x < 0) or (bolaRect.x >= maxDx):
        xVel = - xVel
        boingSom.play()
    
    if (bolaRect.y < 0) or (bolaRect.y >= maxDy):
        yVel = -yVel
        boingSom.play()
    
    bolaRect.x = bolaRect.x + xVel
    bolaRect.y = bolaRect.y +yVel

    # 9 - Limpando janela

    janela.fill(preto)

    # 10 - Carregando assets na janela

    janela.blit(imagemBola, bolaRect)

    # 11 - Atulizando a janela

    pygame.display.update()

    # 12 - Qps

    clock.tick(60)
