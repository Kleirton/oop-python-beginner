import pygame
from pygame.locals import *
import random
from pathlib import Path

# Classe Bola
class Bola():
    def __init__(self, janela, janelaLargura, janelaAltura):
        self.janela = janela # Gurdando a janela em que temos que desenhar mais tarde
        self.janelaLargura = janelaLargura
        self.janelaAltura = janelaAltura

        # Caminho do diretório padrão até a pasta onde está rodando o código
        self.dirBase = Path(__file__).resolve().parent

        # Carregando a imagem da bola

        self.bolaImagem = pygame.image.load(f'{self.dirBase}/imagens/bola.png')

        # Criando o objeto react e definindo [x, y, largura, altura]

        bolaRect = self.bolaImagem.get_rect()
        self.largura = bolaRect.width
        self.altura = bolaRect.height
        self.maxDx = self.janelaLargura - self.largura
        self.maxDy = self.janelaAltura - self.altura

        ## Escolhendo uma posição aleatória
        ### em ambas as direções

        self.x = random.randrange(self.maxDx)
        self.y = random.randrange(self.maxDy)

        ## Escolhendo uma velocidade alteatória entre -4 e 4, exceto 0
        ### em ambas as direções
        listaVel = [-4, -3, -2, -1, 1, 2, 3, 4]

        self.xVel = random.choice(listaVel)
        self.yVel = random.choice(listaVel)

        # Como queremos que ele verifique a posição da bola o tempo todo, 
        # colocamso esse método dentro do método __init__.

    def atulizar(self):
        # verificando se bateu na parede. Se psitivo, mude a direção
        if (self.x < 0) or (self.x >= self.maxDx):
            self.xVel = -self.xVel
            
        if (self.y < 0) or (self.y >= self.maxDy):
            self.yVel = -self.yVel

        # Atulizando a posição da bola utilizando a velodidade nas duas posições. 

        self.x = self.x + self.xVel
        self.y = self.y + self.yVel
    
    # Desenhando a bola na tela

    def desenhar(self):
        self.janela.blit(self.bolaImagem, (self.x, self.y))