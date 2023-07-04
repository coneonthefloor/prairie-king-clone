import os
import pygame
from keyboard import update_keys
from player import Player
from tile_defs import TileDefs
from tilemap import Tilemap

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

tilemap_image_path = os.path.join("assets", "colored_tilemap_packed.png")
tilemap = Tilemap(tilemap_image_path, (8, 8), 0, 0)
tilemap.load()

player = Player()
player_tile = tilemap.get_tile_scaled(TileDefs.PLAYER, (4, 4))


def update(events, delta_time):
    update_keys(events)
    player.update(events, delta_time)


def draw():
    screen.fill(pygame.color.Color(34, 35, 35))

    screen.blit(
        player_tile,
        player.pos,
    )


while running:
    delta_time = clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    update(events, delta_time)
    draw()

    pygame.display.flip()

pygame.quit()
