import os
import pygame
from custom_cursor import CustomCursor
from keyboard import update_keys
from tile_defs import TileDefs
from tilemap import Tilemap


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
RUNNING = True

tilemap_image_path = os.path.join("assets", "tileset.png")
tilemap_image = pygame.image.load(tilemap_image_path)
tilemap = Tilemap(tilemap_image, (16, 16), 0, 1)
tilemap.load()

cursor = CustomCursor(
    tilemap.get_tile_scaled(TileDefs.DIAGONAL_CROSSHAIR, (4, 4)),
    tilemap.get_tile_scaled(TileDefs.DIAGONAL_CROSSHAIR_CLICKED, (4, 4)),
)

goblin_image_original = tilemap.get_tile_scaled(TileDefs.GOBLIN, (6, 6))
goblin_image_squash = tilemap.get_tile_scaled(TileDefs.GOBLIN, (6.2, 5.8))
goblin_image_squeeze = tilemap.get_tile_scaled(TileDefs.GOBLIN, (5.8, 6.2))
goblin_image = goblin_image_original
goblin_rect = goblin_image.get_rect()
goblin_anim_frame = 0
goblin_max_anim_frame = 2
goblin_rect.center = pygame.math.Vector2(
    screen.get_width() // 2, screen.get_height() // 2
)
goblin_speed = 4
goblin_dest = None
goblin_anim_speed = 0.2
goblin_anim_start = pygame.time.get_ticks()


def move_towards(origin, dest, speed):
    return pygame.math.Vector2(*origin).move_towards(dest, speed)


def distance_to(origin, dest):
    return pygame.math.Vector2(*origin).distance_to(dest)


while RUNNING:
    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False

    update_keys(events)

    screen.fill((34, 35, 35))

    screen.blit(goblin_image, goblin_rect)

    if cursor.pressed():
        goblin_dest = cursor.get_pos()

    if goblin_dest:
        goblin_rect.center = move_towards(goblin_rect.center, goblin_dest, goblin_speed)
        seconds = (pygame.time.get_ticks() - goblin_anim_start) / 1000
        if seconds > goblin_anim_speed:
            goblin_anim_start = pygame.time.get_ticks()
            goblin_anim_frame = goblin_anim_frame + 1
            if goblin_anim_frame > goblin_max_anim_frame:
                goblin_anim_frame = 0

            if goblin_anim_frame == 0:
                goblin_image = goblin_image_original
            if goblin_anim_frame == 1:
                goblin_image = goblin_image_squash
            if goblin_anim_frame == 2:
                goblin_image = goblin_image_squeeze
            rect = goblin_rect
            goblin_rect = goblin_image.get_rect()
            goblin_rect.center = rect.center

        if distance_to(goblin_rect.center, goblin_dest) == 0:
            goblin_dest = None
            goblin_anim_start = pygame.time.get_ticks()
            goblin_anim_frame = 0
            goblin_image = goblin_image_original
            rect = goblin_rect
            goblin_rect = goblin_image.get_rect()
            goblin_rect.center = rect.center

    cursor.update()
    cursor.draw(screen)

    pygame.display.flip()

pygame.quit()
