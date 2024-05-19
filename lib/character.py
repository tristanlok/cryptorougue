from enum import Enum
import pygame
import math

from lib.weapon import Weapon, weaponType
import lib.defs as defs

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
    def __init__(self, type):
        # Sprite stuff
        super(Character, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect( center = (defs.SCREEN_WIDTH/2, defs.SCREEN_HEIGHT/2))  # Starting Location
        self.exp = 0
        self.items = []
        self.level = 1
        
        match type:
            case charType.knight_2:
                self.sprite = pygame.image.load("data/character/knight_2.png")
                self.__weapon = weaponType.sword
                self.__health = 10
                self.__damage = 1
                self.__speed = 1
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 10
                self.__player_att_delay = 0
            case charType.knight:
                self.sprite = pygame.image.load("data/character/knight.png")
                self.__weapon = weaponType.sword
                self.__health = 10
                self.__damage = 1
                self.__speed = 1
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 10
                self.__player_att_delay = 0
            case charType.wizard_2:
                self.sprite = pygame.image.load("data/character/wizard_2.png")
                self.__weapon = weaponType.magic
                self.__health = 9
                self.__damage = 2
                self.__speed = 1
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 9
                self.__player_att_delay = 0
            case charType.wizard:
                self.sprite = pygame.image.load("data/character/wizard.png")
                self.__weapon = weaponType.magic
                self.__health = 9
                self.__damage = 2
                self.__speed = 1
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 9
                self.__player_att_delay = 0
            case charType.elf:
                self.sprite = pygame.image.load("data/character/elf.png")
                self.__weapon = weaponType.bow
                self.__health = 8
                self.__damage = 2
                self.__speed = 3
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 8
                self.__player_att_delay = 0
            case charType.pirate:
                self.sprite = pygame.image.load("data/character/pirate.png")
                self.__weapon = weaponType.gun
                self.__health = 12
                self.__damage = 2
                self.__speed = 1
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 12
                self.__player_att_delay = 0
            case charType.fairy:
                self.sprite = pygame.image.load("data/character/fairy.png")
                self.__weapon = weaponType.magic
                self.__health = 6
                self.__damage = 4
                self.__speed = 2
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 6
                self.__player_att_delay = 0
            case charType.cat_girl:
                self.sprite = pygame.image.load("data/character/cat_girl.png")
                self.__weapon = weaponType.sword
                self.__health = 1
                self.__damage = 5
                self.__speed = 3
                self.__attspeed = 1
                self.__add_damage = 0
                self.__mult_damage = 1
                self.__bonus_speed = 10
                self.__bonus_attspeed = 1
                self.__shield = 0
                self.__max_health = 10
                self.__player_att_delay = 0

    def update_pos(self):
        # Movement
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_s]:
            self.rect.y += 2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
            if self.rect.y > 1080 + 75:
                self.rect.y = 0 - 75
        if keys[pygame.K_w]:
            self.rect.y += -2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
            if self.rect.y < 0 - 75:
                self.rect.y = 1080 + 75
        if keys[pygame.K_d]:
            self.rect.x += 2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
            if self.rect.x > 1920 + 75:
                self.rect.x = 0 - 75
        if keys[pygame.K_a]:
            self.rect.x += -2 * (self.get_speed() + 0.1 * math.log(self.get_bonus_speed()))
            if self.rect.x < 0 - 75:
                self.rect.x = 1920 + 75

        self.attack = Weapon(self.get_weapon(), self.rect.x, self.rect.y)

    def get_weapon_hitbox(self):
        return self.attack

    def update_exp(self, amount):
        self.exp += amount
        if self.exp >= 10:
            self.level += 1
            self.exp = 0
            
    def get_level(self):
        return self.level
    
    def add_item(self, item):
        self.items.append(item)
        
    def update_health(self, amount):
        if amount > self.__health + self.__shield:
            gameover = 0
        if amount > self.__shield:
            amount -= self.__shield
            self.__shield = 0
        else:
            self.__shield -= amount
            amount = 0
        self.__health -= amount
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def update_max_health(self, amount):
        self.__max_health += amount

    def set_shield(self, amount):
        self.__shield = amount

    def update_attack_delay(self, int):
        self.__player_att_delay = int

    def get_attack_delay(self):
        return self.__player_att_delay

    def get_weapon(self):
        return self.__weapon

    def update_add_damage(self, amount):
        self.__add_damage += amount
    
    def update_add_damage(self, amount):
        self.__mult_damage *= amount
        
    def update_speed(self, amount):
        self.__bonus_speed += amount
        
    def update_attspeed(self, amount):
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
    
    
    
    