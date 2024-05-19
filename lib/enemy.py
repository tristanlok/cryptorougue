from enum import Enum
import pygame
import random
import math

import lib.defs as defs
from lib.powerup import powerup

class enemyType(Enum):
    monster = 0
    mage = 1
    # tank = 2

class enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super(enemy, self).__init__()
        self.type = type
        self.surf = pygame.Surface((100, 100))
        self.surf.fill([0, 0, 0])

        # Get random location (on the edge)
        if random.randint(0, 1):
            x = random.randint(0, defs.SCREEN_WIDTH)
            y = random.randint(0, 1) * defs.SCREEN_HEIGHT
        else:
            x = random.randint(0, 1) * defs.SCREEN_WIDTH
            y = random.randint(0, defs.SCREEN_HEIGHT)

        self.rect = self.surf.get_rect(
            center = (x, y)
        )

        match type:
            case enemyType.monster:
                self.surf = pygame.Surface((100, 100))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/monster.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 2
                self.__y_speed = 2
                self.__health = 3
            case enemyType.mage:
                self.surf = pygame.Surface((100, 100))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/mage.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 0
                self.__y_speed = 0
                self.__health = 1

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update_pos(self, x, y):
        match self.type:
            case enemyType.monster:
                if x <= self.rect.x:
                    dx = -1
                if x > self.rect.x:
                    dx = 1
                if y <= self.rect.y:
                    dy = -1
                if y > self.rect.y:
                    dy = 1
                self.rect.move_ip(dx, dy)
                if self.rect.right < 0:
                    self.kill()
            case enemyType.mage:
                self.rect.move_ip(self.__x_speed, self.__y_speed)
                if self.rect.right < 0:
                    self.kill()
            
    def update_health(self, amount):
        if amount >= self.__health:
            new_powerup = powerup(self.rect.x, self.rect.y)
            defs.powerups.add(new_powerup) 
            defs.all_sprites.add(new_powerup)
            self.kill()

        else:
            self.__health -= amount
            
    def get_sprite(self):
        return self.sprite