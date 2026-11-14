# 1 - Importando os Pacotes
import pygame
from pygame.locals import *
import sys

# 2 - Definindo as constantes

preto = (0, 0, 0)
largura_janela = 640
altura_janela = 480
quadros_por_segundo = 30

# 3 - Inicializando o "mundo" 
pygame.init()
window = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

# 4 - Carregand recursos (assets)

# 5 - Iniciando variáveis

# 6 - Loop para sempre

while True:

    # 7 - Vericar e tratar eventos
    for event in pygame.event.get():
        # Clicou no botão de fechar? Sai do pygame e finalize o programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Fazendo qualquer ação por frame

    # 9 - Limpar a janela

    window.fill(preto)

    # 10 - Desenhando todos os elementos da janela

    # 11 - Atulziando a janela

    pygame.display.update()

    # 12 - Diminua um pouco o ritmo
    clock.tick(quadros_por_segundo)
