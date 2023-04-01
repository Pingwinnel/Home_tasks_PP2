import pygame 
import random

CARS_SIZE=[100,100]
SIZE=(400,600)
screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Car Game")




pygame.init()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif pygame.event==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-10
            elif event.key==pygame.K_RIGHT:
                x_change=10
            elif event.key==pygame.K_UP:
                y_change=-10
            elif event.key==pygame.K_DOWN:
                y_change=10
            
    screen.fill("WHITE")
    pygame.display.update()