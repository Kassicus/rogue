import pygame

import lib

class Door():
    def __init__(self) -> object:
        pass

class Room():
    def __init__(self) -> object:
        self.background_color = lib.color.get_random_color()

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.background_color, (0, 0, lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT))

    def update(self) -> None:
        pass