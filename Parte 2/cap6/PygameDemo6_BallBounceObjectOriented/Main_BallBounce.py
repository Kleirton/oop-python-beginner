
# 1 - Importando os Pacotes

import pygame
from pygame.locals import *
import sys
import random
from Bola import * # importando todas as classe de Bola.py

# 2 - Definindo as constantes

preto = (0, 0, 0)
janelaLargura = 640
janelaAltura = 480
qps = 60

# 3 - Inicilizando o ambiente

pygame.init()
janela = pygame.display.set_mode((janelaLargura, janelaAltura))
clock = pygame.time.Clock()

# 4 - Carregando recursos (assests)

# 5 - Instânciando variáveis

aBola = Bola(janela, janelaLargura, janelaAltura)

# 6 - Iniciando Loop principal

while True:
    # 7 - Procurando por eventos
    for evento in pygame.event.get():
        # Evento de fecha a janela
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo coisas por quadro

    aBola.atulizar()

    # 9 - Limpando a janela antes desenhar algo de novo

    janela.fill(preto)

    # 10 - Desenhando elementos na tela

    aBola.desenhar()

    # 11 - atulizando a janela

    pygame.display.update()

    # 12 - Desacelerando as coisas

    clock.tick(qps)
