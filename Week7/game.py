import pygame 
import random
import pygame_menu

SIZE_BLOCK=20
WHITE=(255,255,255)
INFOTAB_COLOR=(0,204,153)
COUNT_BLOCKS=20
SNAKE_COLOR=(0,102,0)
MARGIN=1
HEADER_MARGIN=70
BLUE=(204,255,255)
SIZE=[SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS,SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS+HEADER_MARGIN]


class SNAKE_BODY():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    
screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake.exe")
timer=pygame.time.Clock()
def draw_blocks(color,row,column):
    pygame.draw.rect(screen,color,[SIZE_BLOCK+column*SIZE_BLOCK+MARGIN*(column+1),HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK+MARGIN*(row+1),SIZE_BLOCK,SIZE_BLOCK])

snake_blocks=[SNAKE_BODY(9,8),SNAKE_BODY(9,9),SNAKE_BODY(9,10)]
d_col=1
d_row=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and d_col!=0:
                d_row=-1
                d_col=0
            if event.key==pygame.K_DOWN and d_col!=0:
                d_row=1
                d_col=0
            if event.key==pygame.K_LEFT and d_row!=0:
                d_row=0
                d_col=-1
            if event.key==pygame.K_RIGHT and d_row!=0:
                d_row=0
                d_col=1
            

    screen.fill((0,255,204))
    pygame.draw.rect(screen,INFOTAB_COLOR,[0,0,SIZE[0],HEADER_MARGIN])
    
    
    for rows in range(COUNT_BLOCKS):
        for columns in range(COUNT_BLOCKS):
            if (columns+rows)%2==0:
                color=BLUE
            else:
                color=WHITE
            draw_blocks(color,rows,columns)
            
    for block in snake_blocks:
        draw_blocks(SNAKE_COLOR,block.x,block.y)



    head=snake_blocks[-1]
    new_head=SNAKE_BODY(head.x+d_row,head.y+d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)
    timer.tick(2)
    pygame.display.flip()
    
