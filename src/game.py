import os
import pygame
from tile_defs import TileDefs
from tilemap import Tilemap

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

tilemap_image_path = os.path.join("assets", "colored_tilemap_packed.png")
tilemap = Tilemap(tilemap_image_path, (8, 8), 0, 0)
tilemap.load()


def update():
    pass


def draw():
    screen.fill("black")
    screen.blit(
        tilemap.get_tile(TileDefs.PLAYER),
        (screen.get_width() / 2, screen.get_height() / 2),
    )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
