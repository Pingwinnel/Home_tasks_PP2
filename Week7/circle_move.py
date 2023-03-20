import pygame
import os
pygame.init()
screen = pygame.display.set_mode((400, 250))
clock = pygame.time.Clock()


while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        
        pygame.display.update()