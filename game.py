import pygame
import math
from character.character import Character
from enemy import enemy, enemyType
from powerup import powerup, powerupType
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

gameover = 0
shoot_dir = 0
att_delay = 0

player = Character()

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create a custom event for adding a new enemy
ADDPOWERUP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPOWERUP, 250)

# Sprite Groups
player = pygame.sprite.Group() # THIS CAN BE REMOVED LATER
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()

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
        
        # Keydown
        if event.type == KEYDOWN:
            # Movement
            if event.key == K_s:
                dy = 2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_w:
                dy = -2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_d:
                dx = 2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))
            if event.key == K_a:
                dx = -2 * (player.get_speed() + 0.1 * math.log(player.get_bonus_speed()))

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
        elif event.type == KEYUP:
            if event.key == K_s and dy > 0:
                dy = 0
            if event.key == K_w and dy < 0:
                dy = 0
            if event.key == K_d and dx > 0:
                dx = 0
            if event.key == K_a and dx < 0:
                dx = 0

        # Add a new enemy
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = enemy(enemyType.shooter)
            enemies.add(new_enemy)            

        # Add powerup
        elif event.type == ADDPOWERUP:
            # Create the new enemy and add it to sprite groups
            new_powerup = powerups(powerupType.health)
            powerups.add(new_powerup)     
 
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
    screen.blit(player.surf, (x_pos, y_pos))
    
    pygame.draw.circle(screen, (0, 0, 255), (500, 500), 75)

    # Update enemy position
    enemies.update()

    for entity in enemies:
        screen.blit(entity.surf, entity.rect)

    # Draw all sprites
    for entity in powerups:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    # if pygame.sprite.spritecollideany(player, powerups):
    #     # Add collision things here
    #     continue

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()