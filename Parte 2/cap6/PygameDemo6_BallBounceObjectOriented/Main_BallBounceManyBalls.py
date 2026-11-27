# 1 - Importando os pacotes

import pygame
from pygame.locals import *
from Bola import *
import sys

# 2 - Definindo as Constantes

preto = (0, 0, 0)
janelaLargura = 640
janelaAltura = 480
qps = 60
nBolas = 100
listaBolas = []

# 3 - Inicilizando o ambiente

pygame.init()
janela = pygame.display.set_mode((janelaLargura, janelaAltura))
clock = pygame.time.Clock()

# 4 - Carregando recursos (assests)



# 5 - Instânciando variáveis

for x in range(nBolas):
    oBola = Bola(janela, janelaLargura, janelaAltura)

    listaBolas.append(oBola)

# 6 - Iniciando Loop principal

while True:
    # 7 - Dectentando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Fazendo coisas por frame

    for x in range(nBolas):
        listaBolas[x].atulizar()
    
    # 9 - Limpando a tela

    janela.fill(preto)

    # 10 - Desenhando elementos na janela

    for x in range(nBolas):
        listaBolas[x].desenhar()
    
    # 11 - Atulizando a janela 

    pygame.display.update()

    # 12 - Desacelerando um pouco as coisas

    clock.tick(qps)