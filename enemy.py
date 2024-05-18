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
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(-20, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(self.speed, self.speed)
        if self.rect.right < 0:
            self.kill()