from enum import Enum
import pygame
import random
import math

import lib.defs as defs
from lib.powerup import powerup

class enemyType(Enum):
    monster = 0
    mage = 1
    fly = 2
    snake = 3
    big = 4
    dragon = 5
    unicorn = 6

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
                
                self.__x_speed = 1
                self.__y_speed = 1
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
            
            case enemyType.fly:
                self.surf = pygame.Surface((50, 50))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/fly.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 2
                self.__y_speed = 2
                self.__health = 1
                
            case enemyType.snake:
                self.surf = pygame.Surface((100, 100))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/snake.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 2
                self.__y_speed = 1
                self.__health = 1
                
            case enemyType.big:
                self.surf = pygame.Surface((100, 100))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/big.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 1
                self.__y_speed = 1
                self.__health = 5
                
            case enemyType.dragon:
                self.surf = pygame.Surface((200, 200))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/dragon.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 2
                self.__y_speed = 2
                self.__health = 20
                
            case enemyType.unicorn:
                self.surf = pygame.Surface((200, 200))
                self.surf.fill((0, 0, 0))
                self.sprite = pygame.image.load("data/enemy/unicorn.png")
                self.rect = self.surf.get_rect(
                    center = (x, y)
                )
                
                self.__x_speed = 4
                self.__y_speed = 4
                self.__health = 50

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update_pos(self, x, y):
        if x <= self.rect.x:
            dx = -1
        if x > self.rect.x:
            dx = 1
        if y <= self.rect.y:
            dy = -1
        if y > self.rect.y:
            dy = 1
        self.rect.move_ip(dx * self.__x_speed, dy * self.__y_speed)
            
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