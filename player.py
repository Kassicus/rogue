import pygame

import lib
import spell

class Player(pygame.sprite.Sprite):
    def __init__(self) -> pygame.sprite.Sprite:
        super().__init__()

        self.pos = pygame.math.Vector2(float(lib.SCREEN_WIDTH / 2), float(lib.SCREEN_HEIGHT / 2))
        self.vel = pygame.math.Vector2()

        self.move_speed = 300

        self.image = pygame.Surface([40, 40])
        self.image.fill(lib.color.BLUE)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.current_spell = "starter_spell"

        self.spell_list = {
            "starter_spell": spell.StarterSpell
        }

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x = -self.move_speed
        elif keys[pygame.K_d]:
            self.vel.x = self.move_speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y = -self.move_speed
        elif keys[pygame.K_s]:
            self.vel.y = self.move_speed
        else:
            self.vel.y = 0

    def event_loop(self) -> None:
        if pygame.mouse.get_pressed()[0]:
            self.cast_spell(self.current_spell)

    def cast_spell(self, spell: str) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if spell in self.spell_list:
            s = self.spell_list[spell](self.pos.x, self.pos.y, mouse_x, mouse_y)
            lib.active_level.spell_group.add(s)

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.move()
        self.event_loop()

p = Player()