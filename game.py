import ctypes
import random

ctypes.windll.user32.SetProcessDPIAware()

# Custom Libraries
import lib.defs as defs
from lib.character import Character, charType
from lib.enemy import enemy, enemyType
from lib.powerup import powerup, powerupType
from lib.weapon import weaponType

# Initializes Pygame
defs.init()

# Keybinds
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
    bg = defs.pygame.image.load("data/menu/main_menu.png")
    start = defs.pygame.image.load("data/menu/start.png").convert_alpha()
    defs.screen.fill([255, 255, 255])
    defs.screen.blit(bg, (0, 0))
    if transparency < 250 and toggle == 0:
        transparency += 5
    else:
        toggle = 1
        transparency-= 5
        if transparency < 130:
            toggle = 0   
    start.fill((255, 255, 255, transparency), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(start, (0, 400))
    defs.pygame.display.flip()
    
def character_select(hovering):
    defs.screen.fill([0, 0, 0])
    title = defs.pygame.image.load("data/champ_select/select.png")
    defs.screen.blit(title, (0, 0))
    boarder = defs.pygame.image.load("data/champ_select/select_boarder.png")
    
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
    defs.screen.blit(boarder, (x, y))
    
    im0 = defs.pygame.image.load("data/champ_select/knight_2.png")
    im1 = defs.pygame.image.load("data/champ_select/knight.png").convert_alpha()
    im2 = defs.pygame.image.load("data/champ_select/wizard_2.png").convert_alpha()
    im3 = defs.pygame.image.load("data/champ_select/wizard.png").convert_alpha()
    im4 = defs.pygame.image.load("data/champ_select/elf.png").convert_alpha()
    im5 = defs.pygame.image.load("data/champ_select/pirate.png").convert_alpha()
    im6 = defs.pygame.image.load("data/champ_select/fairy.png").convert_alpha()
    im7 = defs.pygame.image.load("data/champ_select/cat_girl.png").convert_alpha()
    
    defs.screen.blit(im0, (500, 350))
    
    if player_data[1] == 0:
        im1.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im1, (750, 350))
    if player_data[2] == 0:
        im2.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im2, (1000, 350))
    if player_data[3] == 0:
        im3.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im3, (1250, 350))
    if player_data[4] == 0:
        im4.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im4, (500, 650))
    if player_data[5] == 0:
        im5.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im5, (750, 650))
    if player_data[6] == 0:
        im6.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im6, (1000, 650)) 
    if player_data[7] == 0:
        im7.fill((255, 255, 255, 50), None, defs.pygame.BLEND_RGBA_MULT)
    defs.screen.blit(im7, (1250, 650))
    
    defs.pygame.display.flip()

def gacha(reward):
    defs.screen.fill([0, 0, 0])
    bg = defs.pygame.image.load("data/gacha/gacha.webp")
    defs.screen.blit(bg, (62,0))
    
    if reward == 1:
        im = defs.pygame.image.load("data/champ_select/cat_girl.png")
        rarity = defs.pygame.image.load("data/gacha/legendary.png")
        player_data[7] = 1
    if reward >=2 and reward <= 6:
        im = defs.pygame.image.load("data/champ_select/fairy.png")
        rarity = defs.pygame.image.load("data/gacha/epic.png")
        player_data[6] = 1
    if reward >= 7 and reward <= 11:
        im = defs.pygame.image.load("data/champ_select/pirate.png")
        rarity = defs.pygame.image.load("data/gacha/epic.png")
        player_data[5] = 1
    if reward >= 12 and reward <= 25:
        im = defs.pygame.image.load("data/champ_select/wizard.png")
        rarity = defs.pygame.image.load("data/gacha/rare.png")
        player_data[3] = 1
    if reward >= 26 and reward <= 39:
        im = defs.pygame.image.load("data/champ_select/wizard_2.png")
        rarity = defs.pygame.image.load("data/gacha/rare.png")
        player_data[2] = 1
    if reward >= 40 and reward <= 54:
        im = defs.pygame.image.load("data/champ_select/elf.png")
        rarity = defs.pygame.image.load("data/gacha/rare.png")
        player_data[4] = 1
    if reward >= 55 and reward <= 100:
        im = defs.pygame.image.load("data/champ_select/knight.png")
        rarity = defs.pygame.image.load("data/gacha/common.png")
        player_data[1] = 1
        
    if reward > 0:    
        defs.screen.blit(im, (860, 500))
        defs.screen.blit(rarity, (0, 0))
        
    defs.pygame.display.flip()

# Display
size = defs.pygame.display.Info()

defs.screen.fill([255, 255, 255])

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
ADDENEMY = defs.pygame.USEREVENT + 1
defs.pygame.time.set_timer(ADDENEMY, 250)

# Create a custom event for adding a new enemy
ADDPOWERUP = defs.pygame.USEREVENT + 1
defs.pygame.time.set_timer(ADDPOWERUP, 1000)

# Sprite Groups
all_sprites = defs.pygame.sprite.Group()
powerups = defs.pygame.sprite.Group()
enemies = defs.pygame.sprite.Group()

player = None

# Game Loop
running = True
while running:
    match menu:
        case 0:
            main_menu(transparency)
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        hovering = 0
                        menu = 2
                    if event.key == K_g:
                        rolling = 0
                        menu = 1
        case 1:
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
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
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
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
                        match hovering:
                            case 0:
                                player = Character(charType.knight_2)
                            case 1:
                                player = Character(charType.knight)
                            case 2:
                                player = Character(charType.wizard_2)
                            case 3:
                                player = Character(charType.wizard)
                            case 4:
                                player = Character(charType.elf)
                            case 5:
                                player = Character(charType.pirate)
                            case 6:
                                player = Character(charType.fairy)
                            case 7:
                                player = Character(charType.cat_girl)
                        all_sprites.add(player)
                        menu = 3
            character_select(hovering)
        case 3:
            if gameover == 1:
                running = False
                
            # Fill the background with white
            defs.screen.fill((255, 255, 255))

            # Quit game if exit
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
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

            # Update enemy position
            for e in enemies:
                e.update_pos()

            # Move player based off of keystroke
            player.update()

            # Update enemy position
            enemies.update()

            # Draw all sprites
            for entity in all_sprites:
                defs.screen.blit(entity.surf, entity.rect)
                defs.screen.blit(entity.get_sprite(), entity.rect)
                
            # Update player
            defs.screen.blit(player.get_sprite(), (x_pos, y_pos))

            # Check if any enemies have collided with the player
            if defs.pygame.sprite.spritecollideany(player, powerups):
                defs.pygame.sprite.spritecollideany(player, powerups).kill()

            # Flip the display
            defs.pygame.display.flip()
                
# Done! Time to quit.
defs.pygame.quit()