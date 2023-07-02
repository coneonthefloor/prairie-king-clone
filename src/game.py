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
    screen.fill(pygame.color.Color(34, 35, 35))

    tile_scale = (4, 4)
    screen.blit(
        tilemap.get_tile_scaled(TileDefs.PLAYER, tile_scale),
        (screen.get_width() / 2, screen.get_height() / 2),
    )

    screen.blit(
        tilemap.get_tile_scaled(TileDefs.DOG, (2, 2)),
        (100, 100),
    )

    screen.blit(
        tilemap.get_tile_scaled(TileDefs.ZOMBIE, tile_scale),
        (600, 400),
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
