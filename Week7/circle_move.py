import pygame
import os
pygame.init()
screen = pygame.display.set_mode((600, 600))
Clock=pygame.time.Clock()

x,y=300,300
speed=20
while True:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_UP:
                                if y-speed<25:
                                        pass
                                else:
                                        y-=speed
                                        
                        if event.key==pygame.K_DOWN:
                                if y+speed>575:
                                        pass
                                else:
                                        y+=speed
                        if event.key==pygame.K_LEFT:
                                if x-speed<25:
                                        pass
                                else:
                                        x-=speed
                        if event.key==pygame.K_RIGHT:
                                if x+speed>575:
                                        pass
                                else:
                                        x+=25
        screen.fill("White")
        pygame.draw.circle(screen,"Red",(x,y),25)
        pygame.display.update()
        Clock.tick(60)
        
        