import pygame

def init():
    # Define constants for the screen width and height
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    global pygame
    pygame.init()

    global screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Sprite Groups
    global all_sprites
    global powerups
    global enemies

    all_sprites = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    enemies = pygame.sprite.Group()