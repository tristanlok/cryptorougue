import pygame
import math
import ctypes
import random

ctypes.windll.user32.SetProcessDPIAware()

# Custom Libraries
from lib.character import Character
from lib.enemy import enemy, enemyType
from lib.powerup import powerup, powerupType
from lib.weapon import Weapon

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
    K_g,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

def main_menu(transparency):
    bg = pygame.image.load("data/menu/main_menu.png")
    start = pygame.image.load("data/menu/start.png").convert_alpha()
    screen.fill([255, 255, 255])
    screen.blit(bg, (0, 0))
    if transparency < 250 and toggle == 0:
        transparency += 5
    else:
        toggle = 1
        transparency-= 5
        if transparency < 130:
            toggle = 0   
    start.fill((255, 255, 255, transparency), None, pygame.BLEND_RGBA_MULT)
    screen.blit(start, (0, 400))
    pygame.display.flip()
    
def character_select(hovering):
    screen.fill([0, 0, 0])
    title = pygame.image.load("data/champ_select/select.png")
    screen.blit(title, (0, 0))
    boarder = pygame.image.load("data/champ_select/select_boarder.png")
    
    if hovering <= 3:
        y = 345
    else:
        y = 645
    if hovering == 0 or hovering == 4:
        x = 495
    if hovering == 1 or hovering == 5:
        x = 745
    if hovering == 2 or hovering == 6:
        x = 995
    if hovering == 3 or hovering == 7:
        x = 1245
    screen.blit(boarder, (x, y))
    
    im0 = pygame.image.load("data/champ_select/knight_2.png")
    im1 = pygame.image.load("data/champ_select/knight.png").convert_alpha()
    im2 = pygame.image.load("data/champ_select/wizard_2.png").convert_alpha()
    im3 = pygame.image.load("data/champ_select/wizard.png").convert_alpha()
    im4 = pygame.image.load("data/champ_select/elf.png").convert_alpha()
    im5 = pygame.image.load("data/champ_select/pirate.png").convert_alpha()
    im6 = pygame.image.load("data/champ_select/fairy.png").convert_alpha()
    im7 = pygame.image.load("data/champ_select/cat_girl.png").convert_alpha()
    
    screen.blit(im0, (500, 350))
    
    if player_data[1] == 0:
        im1.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im1, (750, 350))
    if player_data[2] == 0:
        im2.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im2, (1000, 350))
    if player_data[3] == 0:
        im3.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im3, (1250, 350))
    if player_data[4] == 0:
        im4.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im4, (500, 650))
    if player_data[5] == 0:
        im5.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im5, (750, 650))
    if player_data[6] == 0:
        im6.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im6, (1000, 650)) 
    if player_data[7] == 0:
        im7.fill((255, 255, 255, 50), None, pygame.BLEND_RGBA_MULT)
    screen.blit(im7, (1250, 650))
    
    pygame.display.flip()

def gacha(reward):
    screen.fill([0, 0, 0])
    bg = pygame.image.load("data/gacha/gacha.webp")
    screen.blit(bg, (62,0))
    
    if reward == 1:
        im = pygame.image.load("data/champ_select/cat_girl.png")
        rarity = pygame.image.load("data/gacha/legendary.png")
        player_data[7] = 1
    if reward >=2 and reward <= 6:
        im = pygame.image.load("data/champ_select/fairy.png")
        rarity = pygame.image.load("data/gacha/epic.png")
        player_data[6] = 1
    if reward >= 7 and reward <= 11:
        im = pygame.image.load("data/champ_select/pirate.png")
        rarity = pygame.image.load("data/gacha/epic.png")
        player_data[5] = 1
    if reward >= 12 and reward <= 25:
        im = pygame.image.load("data/champ_select/wizard.png")
        rarity = pygame.image.load("data/gacha/rare.png")
        player_data[3] = 1
    if reward >= 26 and reward <= 39:
        im = pygame.image.load("data/champ_select/wizard_2.png")
        rarity = pygame.image.load("data/gacha/rare.png")
        player_data[2] = 1
    if reward >= 40 and reward <= 54:
        im = pygame.image.load("data/champ_select/elf.png")
        rarity = pygame.image.load("data/gacha/rare.png")
        player_data[4] = 1
    if reward >= 55 and reward <= 100:
        im = pygame.image.load("data/champ_select/knight.png")
        rarity = pygame.image.load("data/gacha/common.png")
        player_data[1] = 1
        
    if reward > 0:    
        screen.blit(im, (860, 500))
        screen.blit(rarity, (0, 0))
        
    pygame.display.flip()
    
pygame.init()

# Display
size = pygame.display.Info()
screen = pygame.display.set_mode((size.current_w, size.current_h), pygame.FULLSCREEN)
screen.fill([255, 255, 255])

#[0-7 = character unlock boolean, 8 = currency]
player_data = [1, 0, 0, 0, 0, 0, 0, 0, 100]

menu = 0
displayed = 0
transparency = 255
toggle = 0
hovering = 0
reward = 0

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

# Create a custom event for adding a new powerup
ADDPOWERUP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPOWERUP, 250)

# Sprite Groups
all_sprites = pygame.sprite.Group()
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Game Loop
running = True
while running:

    match menu:
        case 0:
            main_menu(transparency)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        hovering = 0
                        menu = 2
                    if event.key == K_g:
                        rolling = 0
                        menu = 1
        case 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE and rolling == 0:
                        menu = 0
                if event.type == KEYUP:
                    if event.key == K_SPACE and (player_data[8] > 0 and rolling == 0):
                        player_data[8] -= 1
                        reward = random.randint(1, 100)
                        rolling = 1
                    elif event.key == K_SPACE and rolling == 1:
                        rolling = 0
                        reward = 0
            gacha(reward)   
        case 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_a and (hovering != 0 and hovering != 4):
                        hovering -= 1
                    if event.key == K_d and (hovering != 3 and hovering != 7):
                        hovering += 1
                    if event.key == K_w and hovering > 3:
                        hovering -= 4
                    if event.key == K_s and hovering <= 3:
                        hovering += 4
                    if event.key == K_ESCAPE:
                        menu = 0
                    if event.key == K_SPACE and player_data[hovering] == 1:
                        # Create Player object
                        player = Character()
                        all_sprites.add(player)
                        menu = 3
            character_select(hovering)
        case 3:
            if gameover == 1:
                running = False
                
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
                if event.type == ADDENEMY:
                    new_enemy = enemy(enemyType.shooter)
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)         

                # Add powerup
                if event.type == ADDPOWERUP:
                    new_powerup = powerup(powerupType.health)
                    powerups.add(new_powerup) 
                    all_sprites.add(new_powerup)
        
            if att_delay == 1:
                attack = Weapon(shoot_dir)
                att_delay += 1
            if att_delay > 1 and att_delay < 60:
                screen.blit(attack.surf, (x_pos + attack.get_offset_x(), y_pos + attack.get_offset_y()))
                att_delay += 1
            if att_delay >= 60:
                att_delay += 1
                if att_delay >= 240:
                    att_delay = 0

            x_pos += dx
            y_pos += dy      
            screen.blit(player.surf, (x_pos, y_pos))
            
            pygame.draw.circle(screen, (0, 0, 255), (500, 500), 75)

            # Update enemy position
            enemies.update()

            # Draw all sprites
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)

            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollideany(player, powerups):
                # Add collision things here
                continue

            # Flip the display
            pygame.display.flip()
                
# Done! Time to quit.
pygame.quit()