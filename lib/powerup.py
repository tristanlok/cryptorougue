from enum import Enum
import pygame
import random

import lib.defs as defs

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
                random.randint(0, defs.SCREEN_WIDTH),
                random.randint(0, defs.SCREEN_HEIGHT),
            )
        )
        
    def get_sprite(self):
        return self.sprite