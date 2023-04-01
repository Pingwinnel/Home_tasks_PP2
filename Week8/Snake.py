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
APPLE_NUM=1
pygame.init()
score=0
score_font=pygame.font.SysFont("courier",36)
speed=1

class Apple():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class SNAKE_BODY():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def is_inside(self):
        return -1<=self.x<COUNT_BLOCKS and -1<=self.y<COUNT_BLOCKS
    def __eq__(self,other):
        return isinstance(other,SNAKE_BODY) and self.x==other.x and self.y==other.y
      
        
    
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
            exit()
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
    if  not new_head.is_inside():
        print("Game Over")
        pygame.quit()
        exit()
    elif not new_head.__eq__():
        print("Game Over")
        pygame.quit()
        exit()
    else:
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
    for i in range(APPLE_NUM):
        r_x=random.randint(0,COUNT_BLOCKS-1)
        r_y=random.randint(0,COUNT_BLOCKS-1)
        for i in snake_blocks:
            if i==(r_x,r_y):
                r_x=random.randint(0,COUNT_BLOCKS-1)
                APPLE_NUM+=1
            else:      
                apple=Apple(r_x,r_y)
                APPLE_NUM=0 
    
    
    draw_blocks("Red",apple.x,apple.y)
    
    if new_head.x==apple.x and new_head.y==apple.y:
        score+=1
        APPLE_NUM=1
        speed=score//5+1
        snake_blocks.append(apple)
        
    txt_score=score_font.render("Score: "+str(score),True,WHITE)
    txt_speed=score_font.render("Speed: "+str(speed),True,WHITE)
    screen.blit(txt_score,(SIZE_BLOCK,SIZE_BLOCK))
    screen.blit(txt_speed,(SIZE_BLOCK+230,SIZE_BLOCK))
    timer.tick(3+speed)
    pygame.display.update()