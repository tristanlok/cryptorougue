import pygame
from enum import Enum

import lib.defs as defs

class weaponType(Enum):
    sword = 0
    magic = 1
    bow = 2
    gun = 3

class Weapon(pygame.sprite.Sprite):
    def __init__(self, weapon, x, y):
        super(Weapon, self).__init__()

        self.__x = 0
        self.__y = 0
        self.__offx = 0
        self.__offy = 0

        self.__size_x = 0
        self.__size_y = 0

        if (weapon == weaponType.sword):
            self.melee_attack(x, y)
        
        self.surf = pygame.Surface((self.__size_x, self.__size_y))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect( center = (self.__x + self.__offx, self.__y + self.__offy))

        self.__weapon = weapon

        defs.screen.blit(self.surf, self.rect)

    def melee_attack(self, x , y):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_UP]:
            self.update_size_x(250)
            self.update_size_y(100)

            self.update_x(x)
            self.update_y(y)
            self.update_offx(35)
            self.update_offy(-10)

        if keys[pygame.K_RIGHT]:
            self.update_size_x(100)
            self.update_size_y(250)

            self.update_x(x)
            self.update_y(y)
            self.update_offx(self.__size_x/2 + 40)
            self.update_offy(25)

        if keys[pygame.K_DOWN]:
            self.update_size_x(250)
            self.update_size_y(100)

            self.update_x(x)
            self.update_y(y)
            self.update_offx(35)
            self.update_offy(85)

        if keys[pygame.K_LEFT]:
            self.update_size_x(100)
            self.update_size_y(250)

            self.update_x(x)
            self.update_y(y)
            self.update_offx(-10)
            self.update_offy(25)

    def update_size_x(self, int):
        self.__size_x = int

    def update_size_y(self, int):
        self.__size_y = int

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