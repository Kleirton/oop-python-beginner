
# 1 - Improtando os Pacotes
import pygame
import random
from pygame.locals import * 
import sys
from pathlib import Path

# 2 - Definindo as constantes

preto = (0, 0, 0)
dicBase = Path(__file__).resolve().parent
largura_janela = 640
altura_janela = 480 
bola_largura_altura = 100
maxDx = largura_janela - bola_largura_altura
maxDy = altura_janela - bola_largura_altura
qps = 30 

# 3 - Inicializando ambiente

pygame.init()
janela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

# 4 - Carregando recursos

imagemBola = pygame.image.load(f"{dicBase}/imagens/bola.png")

# 5 - Inicilizando variáveis

bolaX = random.randrange(maxDx)
bolaY = random.randrange(maxDy)
bolaRect = pygame.Rect(bolaX, bolaY, bola_largura_altura, bola_largura_altura)

# 6 - Loop infinito

while True:
    # 7 - Verificar e rastrear eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Se houve clique do mouse
        if evento.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos # Poderia fazer isto se precisarmos disto

            # Verifica se o clique foi na bola
            # Se foi na bola, então escolha um local aleatório
            if bolaRect.collidepoint(evento.pos):
                bolaX = random.randrange(maxDx)
                bolaY = random.randrange(maxDy)
                bolaRect = pygame.Rect(bolaX, bolaY, bola_largura_altura, bola_largura_altura)

    # 8 - Fazendo qualquer coisa por frame

    # 9 - Limpar a tela

    janela.fill(preto)

    # 10 - Desenhando elementos na janela

    janela.blit(imagemBola, (bolaX, bolaY))

    # 11 - Atulizando a janela

    pygame.display.update()

    # 12 - Qps

    clock.tick(qps)
