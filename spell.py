import pygame
import math

import lib

class BaseSpell(pygame.sprite.Sprite):
    def __init__(self,
                 spawn_x: int,
                 spawn_y: int,
                 target_x: int,
                 target_y: int,
                 size: int,
                 speed: float,
                 damage: int,
                 color: pygame.Color
                ) -> pygame.sprite.Sprite:
        super().__init__()

        self.pos = pygame.math.Vector2(spawn_x, spawn_y)
        self.vel = pygame.math.Vector2()

        self.target_pos = pygame.math.Vector2(target_x, target_y)

        self.speed = speed
        self.damage = damage

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        #self.image.set_colorkey(color)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel.x, self.vel.y = self.get_vectors()

    #TODO: Create a function here that overrides or modifies the base image? (I want a circle)

    def get_vectors(self) -> list:
        distance = [self.target_pos.x - self.pos.x, self.target_pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.speed, rate[1] * self.speed]

        return vectors
    
    def check_bounds(self) -> bool:
        if self.pos.x < -100 or self.pos.x > lib.SCREEN_WIDTH + 100:
            return True
        elif self.pos.y < -100 or self.pos.y > lib.SCREEN_HEIGHT + 100:
            return True
        else:
            return False

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        if self.check_bounds():
            self.kill()

class StarterSpell(BaseSpell):
    def __init__(self,
                 spawn_x: int,
                 spawn_y: int,
                 target_x: int,
                 target_y: int,
                ) -> pygame.sprite.Sprite:
        
        self.size = 15
        self.speed = 150
        self.damage = 1
        self.color = lib.color.CYAN

        super().__init__(spawn_x, spawn_y, target_x, target_y, self.size, self.speed, self.damage, self.color)