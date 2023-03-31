import pygame
import os
pygame.init()
screen = pygame.display.set_mode((200, 150))
clock = pygame.time.Clock()
bg=pygame.transform.scale(pygame.image.load("images/bg.jpg"),(200,150))
bt_play=pygame.transform.scale(pygame.image.load("images/bt_play.png"),(20,20))
bt_stop=pygame.transform.scale(pygame.image.load("images/stop.png"),(20,20))
bt_next=pygame.transform.scale(pygame.image.load("images/next.png"),(20,20))
bt_prev=pygame.transform.scale(pygame.image.load("images/prev.png"),(20,20))
music_col=[]
music_num=0
tx_font=pygame.font.SysFont("arial",12)

for filename in os.listdir("music_lib"):
     music_col.append("music_lib/"+filename)

music_info=tx_font.render("None",1,'White','Black')

while True:
        screen.blit(bg,(0,0))
        screen.blit(bt_prev,(20,125))
        screen.blit(bt_play,(60,125))
        screen.blit(bt_stop,(100,125))
        screen.blit(bt_next,(140,125))
        screen.blit(music_info,(20,100))
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        x,y=event.pos        
                        if 80>=x>=60 and 145>=y>=125:
                                pygame.mixer.music.load(music_col[music_num])
                                pygame.mixer.music.play()
                                music_info=tx_font.render(music_col[music_num][10:],1,'White','Black')
                        elif 120>=x>=100 and 145>=y>=125:
                                pygame.mixer.music.stop()
                        elif 40>=x>=20 and 145>=y>=125:
                                if music_num-1==-1:
                                        music_num=len(music_col)-1
                                elif music_num==len(music_col)-1:
                                        music_num=0
                                else:
                                        music_num-=1
                                pygame.mixer.music.load(music_col[music_num])
                                pygame.mixer.music.play()
                                music_info=tx_font.render(music_col[music_num][10:],1,'White','Black')
                        elif 160>=x>=140 and 145>=y>=125:
                                if music_num==len(music_col)-1:
                                        music_num=0
                                else:
                                        music_num+=1
                                pygame.mixer.music.load(music_col[music_num])
                                pygame.mixer.music.play()
                                music_info=tx_font.render(music_col[music_num][10:],1,'White','Black')
                                
                        
        