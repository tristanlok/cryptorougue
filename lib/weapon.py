import pygame
from enum import Enum

class weaponType(Enum):
    sword = 0

class Weapon(pygame.sprite.Sprite):
    def __init__(self, screen, weapon):
        super(self, Weapon).__init__()

        if (weapon == weaponType.sword):
            weapon.melee_attack(screen)
        
        self.__surf = pygame.Surface((self.__x, self.__y))
        self.__surf.fill((255, 0, 0))
        self.__rect = self.__surf.get_rect()

        self.__weapon = weapon


    @staticmethod 
    def melee_attack(self, screen):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_UP]:
            self.__x = 250
            self.__y = 100
            self.__offx = -1 * self.x/2 + 25
            self.__offy = -1 * self.y + 25

        if keys[pygame.K_RIGHT]:
            self.__x = 100
            self.__y = 250
            self.__offx = 25
            self.__offy = -1 * self.y/2 +25

        if keys[pygame.K_DOWN]:
            self.__x = 250
            self.__y = 100
            self.__offx = -1 * self.x/2 + 25
            self.__offy = 25

        if keys[pygame.K_LEFT]:
            self.__x = 100
            self.__y = 250
            self.__offx = -1 * self.x + 25
            self.__offy = -1 * self.y/2 + 25

        screen.blit(self.surf, (self.__x + self.get_offset_x(), self.__y + self.get_offset_y()))