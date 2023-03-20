import pygame

pygame.init()
screen=pygame.display.set_mode([600,800])
pygame.display.set_caption("Clock.exe")
timer=pygame.time.Clock()
image=pygame.image.load("mic2.png")

while True:
    screen.blit(image,(300,400))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break