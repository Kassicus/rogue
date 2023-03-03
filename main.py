import pygame

import lib

pygame.init()

class Game():
    def __init__(self) -> object:
        self.screen = lib.display
        pygame.display.set_caption("Un-named Dungeon Game")

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

    def update(self) -> None:
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()