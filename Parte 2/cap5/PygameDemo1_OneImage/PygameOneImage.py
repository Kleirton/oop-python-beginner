# 0 - Pygame 1, carregando uma imagem na janela

# 1 - Importando os pacotes
import pygame
from pygame.locals import *
import sys
from pathlib import Path

# 2 - Definindo as cosntantes

dicBase = Path(__file__).resolve().parent
preto = (0, 0, 0)
largura_janela = 640
altura_janela = 480
qps = 30

# 3 - Inicializando o ambiente pygame

pygame.init()
janela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

# 4 - Carregando recursos (assets)

imagemBola = pygame.image.load(f'{dicBase}/imagens/bola.png')

# 5 - Variáveis de inicilização

# 6 - Loop para sempre.abs

while True:
    # 7 - Verificando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo qualquer coisa por quadro.

    # 9 - Limpando a janela

    janela.fill(preto)

    # 10 - Desenhando todos os elemtnso da janela. 
    ## Desenhando a bola na posição 100 no eixo x e 200 abaixo no y
    janela.blit(imagemBola, (100, 200))

    # Atulizando a janela

    pygame.display.update()

    # 12 - Desacelerando um pouco as coisas.

    clock.tick(qps) # Fazendo o pygame esperar
