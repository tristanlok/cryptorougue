from enum import Enum
import pygame
import random

import lib.defs as defs

class powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(powerup, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 255, 0))
        self.sprite = pygame.image.load("data/pickups/bitcoin.png")
        self.rect = self.surf.get_rect(
            center=(x, y)
        )
        
    def get_sprite(self):
        return self.sprite