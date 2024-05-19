import pygame

# Custom Libraries
from lib.character import Character
from lib.enemy import enemy, enemyType
from lib.powerup import powerup, powerupType
#from lib.weapon import Weapon

pygame.init()

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

# Display
screen = pygame.display.set_mode([1920, 1080])

x_pos = 500
y_pos = 500
dx = 0
dy = 0

gameover = 0
shoot_dir = 0
att_delay = 0

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create a custom event for adding a new enemy
ADDPOWERUP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPOWERUP, 1000)

# Sprite Groups
all_sprites = pygame.sprite.Group()
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create Player object
player = Character()
all_sprites.add(player)

# Draw reference circle
pygame.draw.circle(screen, (0, 0, 255), (500, 500), 75)

# Game Loop
running = True
while running:

    # Clear Screen
    screen.fill((255, 255, 255))

    if gameover == 1:
        running = 0

    # Quit game if exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add a new enemy
        if event.type == ADDENEMY:
            new_enemy = enemy(enemyType.shooter)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)         

        # Add powerup
        if event.type == ADDPOWERUP:
            new_powerup = powerup(powerupType.health)
            powerups.add(new_powerup) 
            all_sprites.add(new_powerup)

    # Move player based off of keystroke
    player.update(screen)

    # Update enemy position
    enemies.update()

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, powerups):
        # Add collision things here
        pygame.sprite.spritecollideany(player, powerups).kill()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()