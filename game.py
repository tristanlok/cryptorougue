# Custom Libraries
import lib.defs as defs
from lib.character import Character
from lib.enemy import enemy, enemyType
from lib.powerup import powerup, powerupType
from lib.weapon import weaponType

# Initializes Pygame
defs.init()

# defs.pygame.init()
# defs.screen = defs.pygame.display.set_mode([1920, 1080])

# Keybinds
# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_w,
#     K_a,
#     K_s,
#     K_d,
#     K_ESCAPE,
#     KEYDOWN,
#     KEYUP,
#     QUIT,
# )

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

# Create Player object
player = Character(weaponType.sword)
all_sprites.add(player)

# Draw reference circle
defs.pygame.draw.circle(defs.screen, (0, 0, 255), (500, 500), 75)

print("hi")

# Game Loop
running = True
while running:

    # Clear Screen
    defs.screen.fill((255, 255, 255))

    if gameover == 1:
        running = 0

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

    # Move player based off of keystroke
    player.update()

    # Update enemy position
    enemies.update()

    # Draw all sprites
    for entity in all_sprites:
        defs.screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if defs.pygame.sprite.spritecollideany(player, powerups):
        # Add collision things here
        defs.pygame.sprite.spritecollideany(player, powerups).kill()

    # Flip the display
    defs.pygame.display.flip()

# Done! Time to quit.
defs.pygame.quit()