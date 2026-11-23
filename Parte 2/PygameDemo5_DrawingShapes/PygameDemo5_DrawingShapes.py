# 1 - Importando Pacotes

import pygame
from pygame.locals import *
from pathlib import Path
import sys 

# 2 - Definindo constantes

preto = (0, 0, 0)
BLUE = (26, 115, 232)
GREEN = (28, 233, 96)
janela_largura = 640
janela_altura = 480
qps = 60
dirBase = Path(__file__).resolve().parent

# 3 - Inicilizando o ambiente

pygame.init()
janela = pygame.display.set_mode((janela_largura, janela_altura))
clock = pygame.time.Clock()

# 4 - Carregando recursos

# 5 - Instânciando variáveis

# 6 - Loop principal

while True:
    # 7 - Procurando por eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo Coisas por frame

    # 9 - Limpando a tela
    janela.fill(preto)

    # 10 - Desenhando elementos da janela
    ## Desenhando caixas
    pygame.draw.line(janela, BLUE, (20, 20), (60, 20), 4) # topo
    pygame.draw.line(janela, BLUE, (20, 20), (20, 60), 4) # esquerda
    pygame.draw.line(janela, BLUE, (20, 60), (60, 60), 4) # direita
    pygame.draw.line(janela, BLUE, (60, 20), (60, 60), 4) # baixo

    ## Desenhando um X na caixa
    pygame.draw.line(janela, BLUE, (20,20), (60, 60), 1)
    pygame.draw.line(janela, BLUE, (20, 60), (60, 20), 1)

    ## Desenhando um circulo preenchido e um baxio
    pygame.draw.circle(janela, GREEN, (250, 50), 30, 0) # preenchido de verde
    pygame.draw.circle(janela, GREEN, (400, 50), 30, 2) # 2 pixels de borda

    ## Desenhando um retângulo preechindo e um vazio. 

    pygame.draw.rect(janela, (255, 0, 0), (250, 150, 100, 50), 0) # Preenchido
    pygame.draw.rect(janela, (255, 0, 0), (400, 150, 100, 50), 1) # Vazio

    ## Desenhando uma elipse preenchida e uma vazia

    pygame.draw.ellipse(janela, (255, 255, 0), (250, 250, 80, 40), 0) # filled
    pygame.draw.ellipse(janela, (255, 255, 0), (400, 2500, 80, 40), 2) # 2 pixel de borda

    ## Desenhando um hexagono

    pygame.draw.polygon(janela, BLUE, ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410)))

    ## Desenhando um arco

    pygame.draw.arc(janela, BLUE, (20, 400, 100, 100), 0, 2, 5)

    ## DEsenhando anti-aliasing linhas: uma linha, então uma lista de pontos

    pygame.draw.aaline(janela, (255, 0, 0), (500, 400), (540, 470), 1)
    pygame.draw.aalines(janela, (0, 0, 255), True, ((580, 400), ( 587, 450), (595, 460), (600, 444)), 1)

    # 11 - Atulizando a janela 

    pygame.display.update()

    # 12 - Desacelerando as coisas

    clock.tick(qps)
