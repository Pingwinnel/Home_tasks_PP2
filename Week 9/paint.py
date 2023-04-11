import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill("white")
pygame.display.update()
clock = pygame.time.Clock()

red_mode = 'red'
blue_mode = 'blue'
mode = blue_mode
green_mode = 'green'
yellow_mode = (255, 234, 0)

radius = 15
drawing = False
eraser = False
def draw_circle(pos):
    pygame.draw.circle(screen,mode,pos,2*radius,2)
def draw_square(pos):
    x,y = pos
    rect_pos = (x - radius, y - radius)
    rect_size = (2*radius, 2*radius)
    pygame.draw.rect(screen,mode,(rect_pos,rect_size),2)
def draw_right_triangle(pos):
    x,y = pos
    pygame.draw.polygon(screen, mode,[pos, [x, y-2*radius],[x+2*radius, y]],2)
def draw_equilateral_triangle(pos):
    x, y = pos
    height = int(radius * (3 ** 0.5) / 2)
    points = [(x, y - 2*radius), (x - 2*height, y + 2*height), (x + 2*height, y + 2*height)]
    pygame.draw.polygon(screen, mode, points, 2)
def draw_rhombus(pos):
    x, y = pos
    points = [(x, y - radius), (x - radius, y), (x, y + radius), (x + radius, y)]
    pygame.draw.polygon(screen, mode, points, 2)

while True:
    clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_r:
                mode = red_mode
                eraser = False
            elif event.key == pygame.K_b:
                mode = blue_mode
                eraser = False
            elif event.key == pygame.K_g:
                mode = green_mode
                eraser = False
            elif event.key == pygame.K_y:
                mode = yellow_mode
                eraser = False
            elif event.key == pygame.K_s:
                draw_square(pos)
                eraser = False
            elif event.key == pygame.K_c:
                draw_circle(pos)
                eraser = False
            elif event.key == pygame.K_p:
                draw_right_triangle(pos)
                eraser = False
            elif event.key == pygame.K_t:
                draw_equilateral_triangle(pos)
                eraser = False
            elif event.key == pygame.K_h:
                draw_rhombus(pos)
                eraser = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, mode, pos, radius)
                drawing = True
            elif event.button == 3:
                mode = "white"
                eraser = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                mode = blue_mode
                eraser = False
        if event.type == pygame.MOUSEMOTION:
            if drawing and not eraser:
                pygame.draw.circle(screen, mode, pos, radius)
            elif eraser:
                pygame.draw.circle(screen, mode, pos, radius)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                radius += 2
            elif event.y < 0:
                radius -= 2
    pygame.display.update()