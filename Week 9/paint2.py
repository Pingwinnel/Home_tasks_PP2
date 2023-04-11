import pygame
c2=0
c1=0
c3=0
WIDTH=700
HIDTH=700
PIXEL_SIZE=10
BUT_SIZE=(100,200)
ROWS=50
COLS=50
COLORS=["black", "yellow", "red", "green", "blue"]
global grid

def init_grid(rows,cols,color):
    grids=[]
    
    for i in range(rows):
        grids.append([])
        for j in range(cols):
            grids[i].append(color)
    return grids

def grid_draw(screen,grid):
    for i,rows in enumerate(grid):
        for j,col in enumerate(rows):
            pygame.draw.rect(screen,col,(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
    for i in range(ROWS+1):
        pygame.draw.line(screen,'black',(0,i*PIXEL_SIZE),(ROWS*PIXEL_SIZE,i*PIXEL_SIZE))
    for j in range(COLS+1):
        pygame.draw.line(screen,'black',(j*PIXEL_SIZE,0),(j*PIXEL_SIZE,COLS*PIXEL_SIZE))
            
class Button():
    def __init__(self,x,y,width_height,color):
            self.x=x
            self.y=y
            self.width=width_height[0]
            self.height=width_height[1]
            self.color=color
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
    def click(self,pos):
        if (pos[0] > self.x and pos[0] < self.x+self.width and pos[1] > self.y and pos[1] < self.y+self.height) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
        
            
def draw(screen,bg_color):
    screen.fill(bg_color)
    
    grid_draw(screen,grid)
    for i ,col in enumerate(COLORS):
        b1=Button(550,(i*BUT_SIZE[0]),BUT_SIZE,col)
        b1.draw(screen)
    pygame.display.update()

def get_row_col(pos):
     x,y=pos
     row=y//PIXEL_SIZE
     col=x//PIXEL_SIZE
     return row,col
grid=init_grid(ROWS,COLS,"White")
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HIDTH))
    clock = pygame.time.Clock()
    BG_COLOR=(255,255,255)
    drawing_col="black"
    while True:
        draw(screen,BG_COLOR)
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_r:
                    mode = 'red'
                    c1+=10
                elif event.key == pygame.K_g:
                    mode = 'green'
                    c2+=10
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    c3+=10
                elif event.key == pygame.K_c:
                    CIRCLE=not CIRCLE
        
        if pygame.mouse.get_pressed()[0]:
            pos=pygame.mouse.get_pos()
            try:
                row,col=get_row_col(pos)
                grid[row][col]=drawing_col
            except IndexError:
                pass
            else:
                pass
                
        
        pygame.display.flip()
        
        clock.tick(60)
        
        

main()