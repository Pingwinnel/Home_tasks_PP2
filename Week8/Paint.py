import pygame
c2=0
c1=0
c3=0
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    global c1,c2,c3
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    CIRCLE=False
    TRAINGLE=False
    BASE=True
    TXT=True
    ERACE=False
    font_txt=pygame.font.SysFont("arial", 20)
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
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
                    CIRCLE=True
                    TRAINGLE=False
                    ERACE=False
                elif event.key == pygame.K_t:
                    TRAINGLE=True
                    CIRCLE=False
                    ERACE=False
                elif event.key == pygame.K_e:
                    ERACE=True
                    
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        
        if TXT:
                chose_col=font_txt.render("C-circle |T-triagle  |R-red|G-green|B-blue  |Right|left click=Incrase/decrease ", True, "White","Red")
                screen.blit(chose_col, (0,0))
        # draw all points
        i = 0
        if ERACE==True:
            screen.fill("black")
            ERACE=False
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode,CIRCLE,TRAINGLE,BASE,ERACE)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode,circle,train,base,erace):
    global c1,c2,c3
    if color_mode == 'blue':
        color = (c1%255,c2%255,c3%255)
    elif color_mode == 'red':
        color = (c1%255, c2%255, c3%255)
    elif color_mode == 'green':
        color = (c1%255, c2%255, c3%255)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        
            
        if circle:
           pygame.draw.circle(screen, color, (x, y), width)
        if train:
            pygame.draw.rect(screen, color, (x,y,width,width))
                
        

main()