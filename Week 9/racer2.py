
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
COINS=[]
#Setting up FPS 
FPS = 60
COIN_SIZE=(40,40)
Coin_num=1
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE=0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("images/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
                  
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        global COINS
        super().__init__()
        self.r=random.randint(0,2)
        print(self.r)
        if self.r==0:
            self.image=pygame.transform.scale(pygame.image.load("images/coin1.png"),COIN_SIZE)
        elif self.r==1:
            self.image=pygame.transform.scale(pygame.image.load("images/coin2.png"),COIN_SIZE)
        elif self.r==2:
            self.image=pygame.transform.scale(pygame.image.load("images/Coin.png"),COIN_SIZE)
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0) 
        COINS.append(self.image)

        
    def move(self):
        global SCORE
        global COIN_SCORE
        global C2
        self.rect.move_ip(0,5)
        if pygame.sprite.spritecollideany(P1, coins):
            COIN_SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            COINS.clear()
            self.r=random.randint(0,2)
            print(self.r)
            if self.r==0:
                self.image=pygame.transform.scale(pygame.image.load("images/coin1.png"),COIN_SIZE)
            elif self.r==1:
                self.image=pygame.transform.scale(pygame.image.load("images/coin2.png"),COIN_SIZE)
            elif self.r==2:
                self.image=pygame.transform.scale(pygame.image.load("images/Coin.png"),COIN_SIZE)
            COINS.append(self.image)
        elif self.rect.top > 600:
            self.rect.top=0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            COINS.clear()
            self.r=random.randint(0,2)
            print(self.r)
            if self.r==0:
                self.image=pygame.transform.scale(pygame.image.load("images/coin1.png"),COIN_SIZE)
            elif self.r==1:
                self.image=pygame.transform.scale(pygame.image.load("images/coin2.png"),COIN_SIZE)
            elif self.r==2:
                self.image=pygame.transform.scale(pygame.image.load("images/Coin.png"),COIN_SIZE)
            COINS.append(self.image)
            
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C2=Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score: "+str(SCORE), True, BLACK)
    coin_scr = font_small.render("Coins: "+str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scr, (300,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
            
    
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('images/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
