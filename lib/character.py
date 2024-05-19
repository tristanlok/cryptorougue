from enum import Enum
import pygame
import math

from lib.weapon import Weapon

class charType(Enum):
    knight_2 = 0
    knight = 1
    wizard_2 = 2
    wizard = 3
    elf = 4
    pirate = 5
    fairy = 6
    cat_girl = 7

class Character(pygame.sprite.Sprite):
    def __init__(self, type, weapon):
        # Sprite stuff
        super(Character, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        
        match type:
            case charType.knight_2:
                self.sprite = pygame.image.load("data/character/knight_2.png")
            case charType.knight:
                self.sprite = pygame.image.load("data/character/knight.png")
            case charType.wizard_2:
                self.sprite = pygame.image.load("data/character/wizard_2.png")
            case charType.wizard:
                self.sprite = pygame.image.load("data/character/wizard.png")
            case charType.elf:
                self.sprite = pygame.image.load("data/character/elf.png")
            case charType.pirate:
                self.sprite = pygame.image.load("data/character/pirate.png")
            case charType.fairy:
                self.sprite = pygame.image.load("data/character/fairy.png")
            case charType.cat_girl:
                self.sprite = pygame.image.load("data/character/cat_girl.png")
                
        
        # Player data
        self.__health = 10
        self.__damage = 1
        self.__speed = 1
        self.__attspeed = 1
        
        self.__add_damage = 0
        self.__mult_damage = 0
        self.__bonus_speed = 10
        self.__bonus_attspeed = 1
        self.__shield = 0

        self.__player_att_delay = 0

        self.__weapon = weapon

    def update(self):
        # Movement
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_s]:
            self.rect.y += 2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
        if keys[pygame.K_w]:
            self.rect.y += -2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
        if keys[pygame.K_d]:
            self.rect.x += 2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
        if keys[pygame.K_a]:
            self.rect.x += -2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))

        attack = Weapon(self.get_weapon())

        
    def update_health(amount, self):
        if amount > self.__health + self.__shield:
            gameover = 0
        if amount > self.__shield:
            amount -= self.__shield
            self.__shield = 0
        else:
            self.__shield -= amount
            amount = 0
        self.__health -= amount

    def update_attack_delay(self, int):
        self.__player_att_delay = int

    def get_attack_delay(self):
        return self.__player_att_delay

    def get_weapon(self):
        return self.__weapon

    def update_add_damage(amount, self):
        self.__add_damage += amount
    
    def update_add_damage(amount, self):
        self.__mult_damage *= amount
        
    def update_speed(amount, self):
        self.__bonus_speed += amount
        
    def update_attspeed(amount, self):
        self.__bonus_attspeed += amount
        
    def get_health(self):
        return self.__health
    
    def get_damage(self):
        return self.__damage
    
    def get_speed(self):
        return self.__speed
    
    def get_add_damage(self):
        return self.__add_damage
    
    def get_mult_damage(self):
        return self.__mult_damage
    
    def get_bonus_speed(self):
        return self.__bonus_speed
    
    def get_bonus_attspeed(self):
        return self.__bonus_attspeed
    
    def get_sprite(self):
        return self.sprite
    
    
    
    