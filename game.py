import pygame
from enemy import enemy, enemyType

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

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Sprite Groups
enemies = pygame.sprite.Group()

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

        elif event.type == KEYUP:
            if event.key == K_DOWN and dy == 2:
                dy = 0
            if event.key == K_UP and dy == -2:
                dy = 0
            if event.key == K_RIGHT and dx == 2:
                dx = 0
            if event.key == K_LEFT and dx == -2:
                dx = 0

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = enemy(enemyType.shooter)
            enemies.add(new_enemy)            
                
    x_pos += dx
    y_pos += dy      
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos), 75)

    # Update enemy position
    enemies.update()

    for entity in enemies:
        screen.blit(entity.surf, entity.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()