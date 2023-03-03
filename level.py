import pygame

class Level():
    def __init__(self, name: str) -> object:
        self.name = name

        self.spell_group = pygame.sprite.Group()

    def draw(self, surface: pygame.Surface) -> None:
        self.spell_group.draw(surface)

    def update(self) -> None:
        self.spell_group.update()