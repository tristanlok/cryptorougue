import pygame
import math
from character.character import Character

# Keybinds
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

pygame.init()

# Display
screen = pygame.display.set_mode([1920, 1080])

x_pos = 500
y_pos = 500
dx = 0
dy = 0
gameover = 0

player = Character()

# Game Loop
running = True
while running:

    if gameover == 1:
        running = 0
        
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Quit game if exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                dy = 2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_UP:
                dy = -2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_RIGHT:
                dx = 2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_LEFT:
                dx = -2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
        if event.type == KEYUP:
            if event.key == K_DOWN and dy > 0:
                dy = 0
            if event.key == K_UP and dy < 0:
                dy = 0
            if event.key == K_RIGHT and dx > 0:
                dx = 0
            if event.key == K_LEFT and dx < 0:
                dx = 0
            
                
    x_pos += dx
    y_pos += dy      
    screen.blit(player.surf, (x_pos, y_pos))
    
    pygame.draw.circle(screen, (0, 0, 255), (500, 500), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()