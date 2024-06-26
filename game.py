import ctypes
import random

ctypes.windll.user32.SetProcessDPIAware()

# Custom Libraries
import lib.defs as defs
from lib.character import Character, charType
from lib.enemy import enemy, enemyType
from lib.powerup import powerup

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

def roll_item(item):
    if item == 1:
        return defs.pygame.image.load("data/item/sword.png")
    if item == 2:
        return defs.pygame.image.load("data/item/shield.png")
    if item == 3:
        return defs.pygame.image.load("data/item/potion.png")
    if item == 4:
        return defs.pygame.image.load("data/item/boots.png")
    if item == 5:
        return defs.pygame.image.load("data/item/gem.png")
    if item == 6:
        return defs.pygame.image.load("data/item/heart.png")
    
    

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
hit_delay = 0

level = 1
roll_once = 0
once = 0
count = 0

# Create a custom event for adding a new enemy
ADDENEMY = defs.pygame.USEREVENT + 1
defs.pygame.time.set_timer(ADDENEMY, 1000)

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
                        defs.all_sprites.add(player)
                        menu = 3
            character_select(hovering)
        case 3:
            if gameover == 1:
                running = False
            
            # Fill the background with white
            defs.screen.fill((10, 100, 30))

            # Quit game if exit
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
                    running = False

                # Add a new enemy
                if event.type == ADDENEMY:
                    if count < 10:
                        new_enemy = enemy(enemyType.monster)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >=10 and count < 20:
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >=20 and count < 25:
                        new_enemy = enemy(enemyType.monster)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >=25 and count < 35:
                        new_enemy = enemy(enemyType.snake)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >=35 and count < 40:
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 40 and count < 45:
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 45 and count < 47:
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 50 and count < 51:
                        new_enemy = enemy(enemyType.dragon)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 60 and count < 70:
                        new_enemy = enemy(enemyType.monster)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.monster)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.monster)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 70 and count < 80:
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 80 and count < 90:
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 90 and count < 97:
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 100 and count < 103:
                        new_enemy = enemy(enemyType.dragon)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 120 and count < 130:
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.big)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 130 and count < 131:
                        new_enemy = enemy(enemyType.dragon)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.dragon)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 131 and count < 140:
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.fly)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 140 and count < 141:
                        new_enemy = enemy(enemyType.unicorn)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                    if count >= 141 and count < 150:
                        new_enemy = enemy(enemyType.snake)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.snake)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        new_enemy = enemy(enemyType.snake)
                        defs.enemies.add(new_enemy)
                        defs.all_sprites.add(new_enemy)
                        count = 0
                    count += 1  

            # Update enemy position
            for e in defs.enemies:
                e.update_pos(player.rect.x, player.rect.y)

            # Move player based off of keystroke
            player.update_pos()

            # Draw all sprites

            for entity in defs.all_sprites:
                defs.screen.blit(entity.get_sprite(), entity.rect)

            # Check if any enemies have collided with the player
            if defs.pygame.sprite.spritecollideany(player, defs.powerups):
                defs.pygame.sprite.spritecollideany(player, defs.powerups).kill()
                player.update_exp(1)

            # Update Health
            defs.pygame.font.init()
            my_font = defs.pygame.font.SysFont('Ubuntu Light', 30)
            text_surface = my_font.render("Health: " + str(player.get_health()), False, (255, 0, 0))
            defs.screen.blit(text_surface, (10,10))
            text_surface = my_font.render("Shield: " + str(player.get_shield()), False, (0, 0, 255))
            defs.screen.blit(text_surface, (10,40))
            text_surface = my_font.render("Bitcoin: " + str(player.get_exp()) + "/10", False, (0, 255, 0))
            defs.screen.blit(text_surface, (10,70))

            # Check if weapon collides with enemy
            if att_delay == 0:
                if defs.pygame.sprite.spritecollideany(player.get_weapon_hitbox(), defs.enemies):
                    defs.pygame.sprite.spritecollideany(player.get_weapon_hitbox(), defs.enemies).update_health((player.get_damage() + player.get_add_damage()) * player.get_mult_damage())
                att_delay +=1
            if att_delay >=1 :
                att_delay += 1
                if att_delay >= 20:
                    att_delay = 0
            
            # Check if player collides with enemy
            if hit_delay == 0:    
                if defs.pygame.sprite.spritecollideany(player, defs.enemies):
                    defs.pygame.sprite.spritecollideany(player, defs.enemies)
                    player.update_health(1)
                hit_delay += 1
            if hit_delay >= 1:
                hit_delay += 1
                if hit_delay >= 120:
                    hit_delay = 0

            # Check for level up
            if level < player.get_level():
                level = player.get_level()
                menu = 4

            # Check for game end
            if player.get_health() <= 0:
                # player.kill()
                for sprite in defs.all_sprites:
                    sprite.kill()
                menu = 5

            # Flip the display
            defs.pygame.display.flip()
        case 4:
            if roll_once == 0:
                items = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
                imgs = [roll_item(items[0]), roll_item(items[1]), roll_item(items[2])]
                boarder = defs.pygame.image.load("data/champ_select/select_boarder.png")
                anti_boarder = defs.pygame.image.load("data/item/anti_boarder.png")
                blockchain = defs.pygame.image.load("data/item/blockchain.png")
                hovering = 0
                roll_once += 1
            
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_a and hovering != 0:
                        hovering -= 1
                    if event.key == K_d and hovering != 2:
                        hovering += 1
                    if event.key == K_SPACE:
                        match items[hovering]:
                            case 1:
                                player.update_add_damage(1)
                            case 2:
                                player.set_shield(5)
                            case 3:
                                player.update_health(-10)
                            case 4:
                                player.update_speed(1000)
                            case 5:
                                player_data[8] += 1
                            case 6:
                                player.update_max_health(1)
                        player.add_item(items[hovering])
                        roll_once = 0
                        menu = 3
               
            if hovering == 0:
                defs.screen.blit(boarder, (495, 345))
                defs.screen.blit(anti_boarder, (870, 345))   
            elif hovering == 1:
                defs.screen.blit(anti_boarder, (495, 345))
                defs.screen.blit(boarder, (870, 345))  
                defs.screen.blit(anti_boarder, (1245, 345)) 
            else:
                defs.screen.blit(anti_boarder, (870, 345)) 
                defs.screen.blit(boarder, (1245, 345))
                
            defs.screen.blit(imgs[0], (500, 350))
            defs.screen.blit(imgs[1], (875, 350))
            defs.screen.blit(imgs[2], (1250, 350))
            defs.screen.blit(blockchain, (0,0))
            defs.pygame.display.flip()
        case 5:
            defs.screen.fill([0, 0, 0])
            game_over = defs.pygame.image.load("data/menu/game_over.png")
            defs.screen.blit(game_over, (0,0))
            defs.pygame.display.flip()
            for event in defs.pygame.event.get():
                if event.type == defs.pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        level = 1
                        count = 0
                        menu = 0

# Done! Time to quit.
defs.pygame.quit()