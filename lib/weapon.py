import pygame
from enum import Enum

import lib.defs as defs

class weaponType(Enum):
    sword = 0

class Weapon(pygame.sprite.Sprite):
    def __init__(self, weapon):
        super(Weapon, self).__init__()

        self.__x = 0
        self.__y = 0
        self.__offx = 0
        self.__offy = 0

        if (weapon == weaponType.sword):
            self.melee_attack()
        
        self.surf = pygame.Surface((self.__x, self.__y))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

        self.__weapon = weapon

        defs.screen.blit(self.surf, (self.__x + self.__offx, self.__y + self.__offy))

    def melee_attack(self):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_UP]:
            self.update_x(250)
            self.update_y(100)
            self.update_offx(-1 * self.__x/2 + 25)
            self.update_offy(-1 * self.__y + 25)

        if keys[pygame.K_RIGHT]:
            self.update_x(100)
            self.update_y(250)
            self.update_offx(25)
            self.update_offy(-1 * self.__y/2 +25)

        if keys[pygame.K_DOWN]:
            self.update_x(250)
            self.update_y(100)
            self.update_offx(-1 * self.__x/2 + 25)
            self.update_offy(25)

        if keys[pygame.K_LEFT]:
            self.update_x(100)
            self.update_y(250)
            self.update_offx(-1 * self.__x + 25)
            self.update_offy(-1 * self.__y/2 + 25)

    def get_x(self):
        return self.__x
    
    def update_x(self, int):
        self.__x = int
    
    def get_y(self):
        return self.__y
    
    def update_y(self, int):
        self.__y = int
    
    def get_offx(self):
        return self.__offx
    
    def update_offx(self, int):
        self.__offx = int
    
    def get_offy(self):
        return self.__offy
    
    def update_offy(self, int):
        self.__offy = int