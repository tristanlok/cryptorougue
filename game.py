import pygame

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

# Game Loop
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Quit game if exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                dy = 2
            if event.key == K_UP:
                dy = -2
            if event.key == K_RIGHT:
                dx = 2
            if event.key == K_LEFT:
                dx = -2
        if event.type == KEYUP:
            if event.key == K_DOWN and dy == 2:
                dy = 0
            if event.key == K_UP and dy == -2:
                dy = 0
            if event.key == K_RIGHT and dx == 2:
                dx = 0
            if event.key == K_LEFT and dx == -2:
                dx = 0
            
                
    x_pos += dx
    y_pos += dy      
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()