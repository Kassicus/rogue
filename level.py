import pygame

import lib
import room

class Level():
    def __init__(self, name: str) -> object:
        self.name = name

        self.rooms = {
            "spawn_room": room.Room(),
            "second_room": room.Room(),
            "third_room": room.Room()
        }

        self.active_room = self.rooms["spawn_room"]

        self.spell_group = pygame.sprite.Group()

    def draw(self, surface: pygame.Surface) -> None:
        self.active_room.draw(surface)
        self.spell_group.draw(surface)

    def update(self) -> None:
        self.active_room.update()
        self.spell_group.update()