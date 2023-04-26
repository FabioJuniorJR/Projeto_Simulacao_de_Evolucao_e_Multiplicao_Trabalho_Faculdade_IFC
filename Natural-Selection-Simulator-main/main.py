import Classes.entidade as entidade
import Funcoes.pygameHelpers as pygameHelpers
import Classes.food as food
import Classes.simulacao as simulacao
import Variaveis.variaveis as variaveis

import pygame

from math import sin,cos,tan,radians, pi, sqrt


simu = simulacao.simulacao(10, 100, 300)


# Condicional Loop
running = True

# Ciclo do jogo
while running:
    #pygameHelpers.pause(variaveis.screen)


    # Checa a stack de eventos
    # pygame.QUIT é o evento de clicar no X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Configurando pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygameHelpers.pause(variaveis.screen)         

    # apaga o ultimo frame enxendo a tela de preto
    variaveis.screen.fill("black")

    # Desenha Arena
    simu.desenhaArena()    
    
    simu.DrawCircolos()


    # Desenha Comida 
    simu.desenhaComida()
            
    # Desenha Entidades e Calcula Colisoes
    
    #   Simu.tick()
        #   Desenha Entidades

        #   Move Entidades

            #   Devora comida
    
    simu.tick()
    

    simu.DrawEmisferios()
    # Trocando o buffer para aparecer oque foi desenhado
    pygame.display.flip()

    variaveis.clock.tick(60)  # Limite de FPS

pygame.quit()