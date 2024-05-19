import pygame

def init():
    global pygame
    pygame.init()

    global screen
    screen = pygame.display.set_mode([1920, 1080])