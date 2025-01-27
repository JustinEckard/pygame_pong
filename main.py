import pygame
from pygame.locals import *

pygame.init()

screen_width = 600;
screen_height = 500;

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game variables

font = pygame.font.SysFont('Sans Serif', 32)
margin = 50
cpu_score = 0 
player_score = 0 


# Colors

bg = (120, 100 , 130)
white =  (255, 255, 255)

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin) , (screen_width, margin))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Game loop

run = True
while run:

    draw_board() # This fills the background
    draw_text('CPU: ' + str(cpu_score), font , white , 20, 15)
    draw_text('P1: ' + str(player_score), font , white , screen_width - 100, 15)
    # Event Handler to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # This makes the changes in the code actually display
pygame.quit()
