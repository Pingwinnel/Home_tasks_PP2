import pygame
import os
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Game')

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
BOXES_NUM=1

HEALTH_FONT=pygame.font.SysFont('comicsans',20)
BULLETS_FONT=pygame.font.SysFont('comicsans',20)
WINNER_FONT=pygame.font.SysFont('comicsans',100)

FPS=60
VEL=20
BULLET_VEL=25
MAX_BULLETS=3000

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)



BULLET_HIT_SOUND=pygame.mixer.Sound('hackaton/Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND=pygame.mixer.Sound('hackaton/Assets/Gun+Silencer.mp3')
HEAL_SOUND=pygame.mixer.Sound('hackaton/Assets/heal.mp3')
POWER_SOUND=pygame.mixer.Sound('hackaton/Assets/power.mp3')
#BULLET_FIRE_SOUND1=pygame.mixer.Sound(os.path.join('Assets','TFU2.mp3'))
#BULLET_FIRE_SOUND2=pygame.mixer.Sound(os.path.join('Assets','chort0.mp3'))


SHIP_WIDTH=50
SHIP_HEIGHT=45

YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2
BOXE=pygame.USEREVENT+3
EFFECT=pygame.USEREVENT+4
DAMAGE_R=pygame.USEREVENT+5
YELLOW_GET=pygame.USEREVENT+6
RED_GET=pygame.USEREVENT+7
DAMAGE_Y=pygame.USEREVENT+8
HEAL_Y=pygame.USEREVENT+9
HEAL_R=pygame.USEREVENT+10


img_b=["bullet.png","aid.png"]
box_img=[]
for i in img_b:
    box_img.append("hackaton/Assets/"+i)

SPACE_PIC=pygame.image.load('hackaton/Assets/space.png')
Yellow_Spaceship_pic=pygame.image.load('hackaton/Assets/ships/spaceship_yellow.png' )
Red_Spaceship_pic=pygame.image.load('hackaton/Assets/ships/spaceship_red.png')
PLAYER="P1"

class Boxes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.r=random.randint(0,1)
        if self.r==0:
            self.image = pygame.transform.scale(pygame.image.load(box_img[self.r]).convert_alpha(), (50, 50))
        elif self.r==1:
           self.image = pygame.transform.scale(pygame.image.load(box_img[self.r]).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50,800-75),random.randint(50,800-50)) 
    def gotboxe(self):
        self.rect.center = (random.randint(50,800-50),random.randint(50,800-50))

        
def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()/2,HEIGHT//2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    menu()
    

                
        
        

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,boxes):
    WIN.blit(SPACE_PIC,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    
    red_health_txt=HEALTH_FONT.render('HEALTH: '+ str(red_health),1,WHITE)
    yellow_health_txt=HEALTH_FONT.render('HEALTH: '+ str(yellow_health),1,WHITE)
    
    red_bullets_display=BULLETS_FONT.render('BULLETS: '+str(len(red_bullets)),1,WHITE)
    yellow_bullets_display=BULLETS_FONT.render('BULLETS: '+str(len(yellow_bullets)),1,WHITE)

    
    WIN.blit(red_health_txt,(WIDTH-red_health_txt.get_width()-10,10))
    WIN.blit(yellow_health_txt,(10,10))
    
    WIN.blit(red_bullets_display,(WIDTH-red_bullets_display.get_width()-12,30))
    WIN.blit(yellow_bullets_display,(10,30))

    
    WIN.blit(Yellow_Spaceship,(yellow.x,yellow.y))
    WIN.blit(Red_Spaceship,(red.x,red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    for boxe in boxes:
        WIN.blit(boxe.image, boxe.rect)  

    pygame.display.update()

def movement(keys_pressed,yellow,red):
    #YELLOW
    if keys_pressed[pygame.K_a] and yellow.x-VEL>=0: #LEFT
            yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL<=430: #RIGHT
            yellow.x+=VEL
    #if keys_pressed[pygame.K_q]: #RIGHT-BOOST
            #yellow.x+=VEL+15
    if keys_pressed[pygame.K_w] and yellow.y-VEL>=0: #UP
            yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL<=450: #DOWN
            yellow.y+=VEL
    #RED
    if keys_pressed[pygame.K_KP4] and red.x-VEL>=430: #LEFT
            red.x-=VEL
    #if keys_pressed[pygame.K_KP7]: #LEFT-BOOST
            #red.x-=VEL+15
    if keys_pressed[pygame.K_KP6] and red.x+VEL<=850: #RIGHT
            red.x+=VEL
    if keys_pressed[pygame.K_KP8] and red.y-VEL>=0: #UP
            red.y-=VEL
    if keys_pressed[pygame.K_KP5] and red.y+VEL<=450: #DOWN
            red.y+=VEL
            
def handle_bullets(red_bullets,yellow_bullets,red,yellow,damageY,damageR):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet) and damageY=="yellow":
            pygame.event.post(pygame.event.Event(RED_HIT))
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        if yellow.colliderect(bullet) and damageR=="red":
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
    
def handle_boxes(boxes,red,yellow):
        for boxe in boxes:
            if red.colliderect(boxe) and boxe.r==0:
                pygame.event.post(pygame.event.Event(RED_GET))
                POWER_SOUND.play()
                boxes.remove(boxe)
            elif yellow.colliderect(boxe) and boxe.r==0:
                pygame.event.post(pygame.event.Event(YELLOW_GET))
                POWER_SOUND.play()
                boxes.remove(boxe)
            elif yellow.colliderect(boxe) and boxe.r==1:
                pygame.event.post(pygame.event.Event(HEAL_Y))
                boxes.remove(boxe)
            elif red.colliderect(boxe) and boxe.r==1:
                pygame.event.post(pygame.event.Event(HEAL_R))
                boxes.remove(boxe)
def main():
    global Yellow_Spaceship,Yellow_Spaceship_pic,Red_Spaceship_pic,Red_Spaceship
    
    Yellow_Spaceship=pygame.transform.rotate(pygame.transform.scale(Yellow_Spaceship_pic,(SHIP_WIDTH,SHIP_HEIGHT)),270)
    Red_Spaceship=pygame.transform.rotate(pygame.transform.scale(Red_Spaceship_pic,(SHIP_WIDTH,SHIP_HEIGHT)), 90)
    red=pygame.Rect(700,300,SHIP_WIDTH,SHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SHIP_WIDTH,SHIP_HEIGHT)
    global BOXES_NUM
    pygame.time.set_timer(BOXE,10000)
    
    red_bullets=[]
    yellow_bullets=[]
    boxes=[]
    damage_Y="none"
    damage_R="none"
    red_health=10
    yellow_health=10

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==BOXE:
                B1=Boxes()
                boxes.append(B1)
            if event.type ==pygame.QUIT:
                run=False
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_e and len(yellow_bullets)<MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_KP9 and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
            if event.type==RED_HIT:
                    red_health-=1
                    BULLET_HIT_SOUND.play()
            if event.type==YELLOW_HIT:
                yellow_health-=1
                BULLET_HIT_SOUND.play()
                
            
            if event.type==YELLOW_GET:
                pygame.time.set_timer(DAMAGE_Y,5000,0)
                damage_Y="yellow"
            if event.type==RED_GET:
                pygame.time.set_timer(DAMAGE_R,5000,0)
                damage_R="red"
            
            if event.type==DAMAGE_Y:
                damage_Y="none"
                pygame.time.set_timer(DAMAGE_Y,0,0) 
            elif event.type==DAMAGE_R:
                damage_R="none"
                pygame.time.set_timer(DAMAGE_R,0,0) 
                
            if event.type==HEAL_R:
                red_health+=2
                HEAL_SOUND.play()
            elif event.type==HEAL_Y:
                yellow_health+=2 
                HEAL_SOUND.play()    
                
            winner_txt=""
            if red_health<=0:
                winner_txt="YELLOW WINS"
                
                        
            if yellow_health<=0:
                winner_txt="RED WINS"
                
            
            if winner_txt!="":
                draw_winner(winner_txt)
                red_health=10
                yellow_health=10
                break
            
                
        keys_pressed=pygame.key.get_pressed()
        
        handle_bullets(red_bullets,yellow_bullets,red,yellow,damage_Y,damage_R)
        
        handle_boxes(boxes,red,yellow)
        
        movement(keys_pressed,yellow,red)
        
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,boxes)
        pygame.display.update()
 
 


def custom():
    global PLAYER
    global Yellow_Spaceship_pic,Red_Spaceship_pic
    Run=True
    bg=pygame.image.load("hackaton/Assets/BG1.jpg")
    menu_font=pygame.font.Font("hackaton/Assets/8bit.ttf",100)
    info=menu_font.render("Choose your skin "+ PLAYER,1,"White")
    info_save=menu_font.render("Save",1,"Green")
    bt_next=pygame.transform.scale(pygame.image.load("hackaton/Assets/next.png"),(75,75))
    bt_prev=pygame.transform.scale(pygame.image.load("hackaton/Assets/prev.png"),(75,75))
    skins=[]
    
    
    for filename in os.listdir("hackaton/Assets/ships"):
        skins.append("hackaton/Assets/ships/"+filename)
    
    i=0
    while Run:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and 165<pos[0]<240 and 150<pos[1]<150+75: 
                    if i-1==-1:
                        i=len(skins)-1
                    elif i==len(skins):
                        i=0
                    else:
                        i-=1
                elif pygame.mouse.get_pressed()[0] and 660<pos[0]<735 and 150<pos[1]<150+75:
                    if i==len(skins)-1:
                        i=0
                    else:
                        i+=1
                elif pygame.mouse.get_pressed()[0] and (WIDTH//2-info_save.get_width()/2)<pos[0]<info_save.get_width()+(WIDTH//2-info_save.get_width()/2) and (5)<pos[1]<(info_save.get_height()+5):    
                    if PLAYER=="P1":
                        Yellow_Spaceship_pic=pygame.image.load(skins[i])
                        PLAYER="P2"
                        custom()
                    else:
                        Red_Spaceship_pic=pygame.image.load(skins[i])
                        menu()
                    
                    
                    
                    
                    
        WIN.fill((255,255,255))
        WIN.blit(bg,(0,0))
        WIN.blit(info,(WIDTH//2-info.get_width()/2,400))
        WIN.blit(info_save,(WIDTH//2-info_save.get_width()/2,5))
        WIN.blit(pygame.transform.scale(pygame.image.load(skins[i]),(400,300)),(250,75))
        WIN.blit(bt_next,(660,150))
        WIN.blit(bt_prev,(165,150))
        
        pygame.display.update()
        
        
          
def menu():
    Run=True
    bg=pygame.image.load("hackaton/Assets/BG1.jpg")
    menu_font=pygame.font.Font("hackaton/Assets/8bit.ttf",100)
    playtx=menu_font.render("Play",1,"White")
    quittx=menu_font.render("Quit",1,"White")
    customtx=menu_font.render("Customize",1,"White")
    while Run:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and (WIDTH//2-playtx.get_width()/2)<pos[0]<playtx.get_width()+(WIDTH//2-playtx.get_width()/2) and (HEIGHT//2-playtx.get_height()/2  -75)<pos[1]<(HEIGHT//2-playtx.get_height()/2  -75)+playtx.get_height():
                    main()
                elif pygame.mouse.get_pressed()[0] and (WIDTH//2-quittx.get_width()/2)<pos[0]<(WIDTH//2-quittx.get_width()/2)+quittx.get_width() and (HEIGHT//2-quittx.get_height()/2 + 125)<pos[1]<(HEIGHT//2-quittx.get_height()/2 + 125)+quittx.get_height():
                    pygame.quit()
                    exit()
                elif pygame.mouse.get_pressed()[0] and (WIDTH//2-customtx.get_width()/2)<pos[0]<(WIDTH//2-customtx.get_width()/2)+customtx.get_width() and (HEIGHT//2-customtx.get_height()/2 + 25)<pos[1]<(HEIGHT//2-customtx.get_height()/2 + 25)+customtx.get_height():
                    custom()
                    
        WIN.fill((255,255,255))
        WIN.blit(bg,(0,0))
        WIN.blit(playtx,(WIDTH//2-playtx.get_width()/2,HEIGHT//2-playtx.get_height()/2  -75))
        WIN.blit(quittx,(WIDTH//2-quittx.get_width()/2,HEIGHT//2-quittx.get_height()/2 + 125))
        WIN.blit(customtx,(WIDTH//2-customtx.get_width()/2,HEIGHT//2-customtx.get_height()/2 + 25))
        pygame.display.update()
        
menu()