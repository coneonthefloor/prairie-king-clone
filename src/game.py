import os
import sys
import pygame
from constants import FRAME_RATE, HEIGHT, WIDTH
from game_object import GameObject
from tilemap import Tilemap


background_image = pygame.image.load(os.path.join("assets", "back.png"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

clouds_image = pygame.image.load(os.path.join("assets", "clouds.png"))
clouds_image = pygame.transform.scale(clouds_image, (WIDTH, HEIGHT))

cloud1 = GameObject(clouds_image, 1)
cloud2 = GameObject(clouds_image, 1)
cloud2.pos.x = WIDTH

ground_tile_sheet =pygame.image.load(os.path.join("assets", "sheet.png"))
tilemap = Tilemap(ground_tile_sheet, (16, 16), 0, 0)
tilemap.load()

ground1 = tilemap.get_tile_scaled((7, 2), (5, 5))
ground2 = tilemap.get_tile_scaled((7, 3), (5, 5))
ground3 = tilemap.get_tile_scaled((11, 1), (5, 5))
ground_tile_width = ground1.get_width()
ground_tile_count = WIDTH // ground_tile_width


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

            cloud1.move(left=True)
            cloud2.move(left=True)
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(cloud1.image, cloud1.pos)
            self.screen.blit(cloud2.image, cloud2.pos)
            for i in range(0, ground_tile_count):
                self.screen.blit(ground1, (ground1.get_width() * i, HEIGHT - ground1.get_height() * 2))
                if i % 5 == 0:
                    self.screen.blit(ground2, (ground2.get_width() * i, HEIGHT - ground2.get_height()))
                else:
                    self.screen.blit(ground3, (ground3.get_width() * i, HEIGHT - ground3.get_height()))
            pygame.display.flip()


if __name__ == "__main__":
    Game().run()
