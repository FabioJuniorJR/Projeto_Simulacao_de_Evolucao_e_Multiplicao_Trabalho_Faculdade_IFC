import numpy as np
import pygame
from math import cos, sin, sqrt

class Food:
    
    def __init__(self, screen, raioArena, posicaoInicial):
        
        raioComida = np.random.randint(10,raioArena * (4/5))
        anguloComida = np.random.randint(0,361)
        
        # Atributos
        self.x = cos(anguloComida) * raioComida + posicaoInicial[0]
        self.y = posicaoInicial[1] - sin(anguloComida) * raioComida
        self.screen = screen
        self.radius = 5
        self.devorada = False

        #   Atributo arena
        self.raioArena = raioArena

        # TEMP
        self.cor = "orange"

        # Spawn SemiAleatorio
        self.spawnSemiAleatorio(posicaoInicial)

    def spawnSemiAleatorio(self, posicaoInicial, recursivo = False):
        if recursivo:
            raioComida = np.random.randint(60, self.raioArena * (4/5))
            anguloComida = np.random.randint(0,361)
            self.x = cos(anguloComida) * raioComida + posicaoInicial[0]
            self.y = posicaoInicial[1] - sin(anguloComida) * raioComida

        if abs(self.x - posicaoInicial[0]) <= 15:
            if self.x > posicaoInicial[0]:
                self.x += np.random.randint(15, 20)

            elif self.x <= posicaoInicial[0]:
                self.x -= np.random.randint(15, 20)

        if abs(self.y - posicaoInicial[1]) <= 15:
            if self.y > posicaoInicial[1]:
                self.y += np.random.randint(15, 20)

            elif self.y <= posicaoInicial[1]:
                self.y -= np.random.randint(15, 20)

        distancia = sqrt((posicaoInicial[0] - self.x) ** 2 + (posicaoInicial[1] - self.y) ** 2)

        for i in range(0,5):
            if abs(distancia - (300 - (60 * i))) <= 15:                
                self.spawnSemiAleatorio(posicaoInicial, recursivo=True)

    def draw(self):
        pygame.draw.circle(self.screen, self.cor, [self.x,self.y], self.radius)
        
    def getPosition(self):
        return [self.x, self.y, self.radius]

    def foiDevorada(self):
        return self.devorada