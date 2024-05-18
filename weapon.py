import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, rotation):
        super(Weapon, self).__init__()
        match rotation:
            case 1:
                self.x = 250
                self.y = 100
                self.offx = -1 * self.x/2
                self.offy = -1 * self.y
            case 2:
                self.x = 100
                self.y = 250
                self.offx = 0
                self.offy = -1 * self.y/2
            case 3:
                self.x = 250
                self.y = 100
                self.offx = -1 * self.x/2
                self.offy = 0
            case 4:
                self.x = 100
                self.y = 250
                self.offx = -1 * self.x
                self.offy = -1 * self.y/2
        self.surf = pygame.Surface((self.x, self.y))
        self.surf.fill((255, 0, 0))
        
    def get_offset_x(self):
        return self.offx
    
    def get_offset_y(self):
        return self.offy
        
