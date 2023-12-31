import os
import sys
import pygame
from clouds import Clouds
from constants import FLOOR, FRAME_RATE, HEIGHT, WIDTH
from ground import Ground
from player import Player


background_image = pygame.image.load(os.path.join("assets", "back.png"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

clouds = Clouds()
ground = Ground(FLOOR)
player = Player()


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FRAME_RATE)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.screen.blit(background_image, (0, 0))

            clouds.update()
            clouds.draw(self.screen)

            player.update()
            player.draw(self.screen)

            ground.update()
            ground.draw(self.screen)

            pygame.display.flip()


if __name__ == "__main__":
    Game().run()
