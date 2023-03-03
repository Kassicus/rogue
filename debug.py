import pygame

import lib

class DebugInterface():
    def __init__(self) -> object:
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.fps_text = None
        self.mouse_text = None
        self.alive_projectile_text = None

        self.fps_offset = 0
        self.mouse_offset = 0
        self.alive_projectile_offset = 0

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        fps_string = "FPS: " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, True, lib.color.WHITE)

        fps_offset = int(lib.SCREEN_WIDTH - fps_text.get_width() - 10)

        return fps_text, fps_offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_string = "Mouse (X: " + str(mouse_x) + " | Y: " + str(mouse_y) + ")"
        mouse_text = self.font.render(mouse_string, True, lib.color.WHITE)

        mouse_offset = int(lib.SCREEN_WIDTH - mouse_text.get_width() - 10)

        return mouse_text, mouse_offset
    
    def get_alive_projectiles(self) -> list [pygame.Surface, int]:
        alive_projectiles_string = "Projectiles: " + str(len(lib.active_level.spell_group))
        alive_projectiles_text = self.font.render(alive_projectiles_string, True, lib.color.WHITE)

        alive_projectiles_offset = int(lib.SCREEN_WIDTH - alive_projectiles_text.get_width() - 10)

        return alive_projectiles_text, alive_projectiles_offset

    def draw_center(self, surface: pygame.Surface) -> None:
        pygame.draw.line(surface, lib.color.GREEN, (lib.SCREEN_WIDTH / 2, 0), (lib.SCREEN_WIDTH / 2, lib.SCREEN_HEIGHT))
        pygame.draw.line(surface, lib.color.RED, (0, lib.SCREEN_HEIGHT / 2), (lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT / 2))

    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.fps_text, (self.fps_offset, 10))
        surface.blit(self.mouse_text, (self.mouse_offset, 30))
        surface.blit(self.alive_projectile_text, (self.alive_projectile_offset, 50))

        self.draw_center(surface)

    def update(self, clock: pygame.time.Clock) -> None:
        self.fps_text, self.fps_offset = self.get_fps(clock)
        self.mouse_text, self.mouse_offset = self.get_mouse()
        self.alive_projectile_text, self.alive_projectile_offset = self.get_alive_projectiles()