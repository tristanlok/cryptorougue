from enum import Enum
import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class enemyType(Enum):
    shooter = 0
    fighter = 1
    tank = 2

class enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super(enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.__x_speed = random.randint(-2, 2)
        self.__y_speed = random.randint(-2, 2)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(self.__x_speed, self.__y_speed)
        if self.rect.right < 0:
            self.kill()