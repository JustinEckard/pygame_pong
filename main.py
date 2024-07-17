import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# This is the view for the game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300,250,50,50))

# Game Loop
run = True;

while run:
    screen.fill((110,40,20))
    pygame.draw.rect(screen,(255,230,22),player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # this is an event handler and checks input
            run = False

    pygame.display.update()

pygame.QUIT()