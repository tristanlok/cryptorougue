import pygame
from weapon import Weapon

# Keybinds
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
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
shoot_dir = 0
att_delay = 0

# Game Loop
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Quit game if exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keydown
        if event.type == KEYDOWN:
            
            # Movement
            if event.key == K_s:
                dy = 2
            if event.key == K_w:
                dy = -2
            if event.key == K_d:
                dx = 2
            if event.key == K_a:
                dx = -2
            # Attacking
            if att_delay == 0:
                if event.key == K_UP:
                    shoot_dir = 1
                    att_delay = 1
                elif event.key == K_RIGHT:
                    shoot_dir = 2
                    att_delay = 1
                elif event.key == K_DOWN:
                    shoot_dir = 3
                    att_delay = 1
                elif event.key == K_LEFT:
                    shoot_dir = 4
                    att_delay = 1
                
        # Keyup    
        if event.type == KEYUP:
            if event.key == K_s and dy > 0:
                dy = 0
            if event.key == K_w and dy < 0:
                dy = 0
            if event.key == K_d and dx > 0:
                dx = 0
            if event.key == K_a and dx < 0:
                dx = 0
 
    if att_delay == 1:
        attack = Weapon(shoot_dir)
        att_delay += 1
    if att_delay > 1:
        screen.blit(attack.surf, (x_pos + attack.get_offset_x(), y_pos + attack.get_offset_y()))
        att_delay += 1
        if att_delay >= 60:
            att_delay = 0

 
    x_pos += dx
    y_pos += dy      
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()