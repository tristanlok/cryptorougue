from enum import Enum
import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class powerupType(Enum):
    health = 0
    damage = 1
    speed = 2


class powerup(pygame.sprite.Sprite):
    def __init__(self, type):
        super(powerup, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 255, 0))
        self.sprite = pygame.image.load("data/pickups/bitcoin.png")
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        
    def get_sprite(self):
        return self.sprite