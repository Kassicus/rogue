import pygame
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class Color():
    def __init__(self) -> object:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

    def get_random_color(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c

color = Color()    
display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

events = pygame.event.get()

delta_time = 0
fps_limit = 120