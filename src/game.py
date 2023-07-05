import os
import pygame
from keyboard import update_keys
from entities.cursor import Cursor
from entities.player import Player
from tile_defs import TileDefs
from tilemap import Tilemap

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

tilemap_image_path = os.path.join("assets", "tileset.png")
tilemap_image = pygame.image.load(tilemap_image_path)
tilemap = Tilemap(tilemap_image, (16, 16), 0, 1)
tilemap.load()

player_tile = tilemap.get_tile_scaled(TileDefs.MINI_WIZ, (8, 8))
player = Player(player_tile)
player.pos.x = screen.get_width() / 2
player.pos.y = screen.get_height() / 2

cursor = Cursor(tilemap, (2, 2))


def update(events, delta_time):
    update_keys(events)
    player.update(events, delta_time)
    cursor.update(events, delta_time)


def draw():
    screen.fill((34, 35, 35))
    player.draw(screen)
    cursor.draw(screen)


while running:
    delta_time = clock.tick(60)
    events = pygame.event.get()
    cursor_position = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    update(events, delta_time)
    draw()

    pygame.display.flip()

pygame.quit()
