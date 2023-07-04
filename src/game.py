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

player_tile = tilemap.get_tile_scaled(TileDefs.PLAYER, (4, 4))
player = Player(player_tile)
player.pos.x = screen.get_width() / 2
player.pos.y = screen.get_height() / 2


LERP_FACTOR = 0.05
minimum_distance = 40
maximum_distance = 100

dog_tile = tilemap.get_tile_scaled(TileDefs.DOG, (2, 2))
dog = pygame.math.Vector2(
    player.pos.x - minimum_distance, player.pos.y - minimum_distance
)


def FollowMe(pops, fpos):
    target_vector = pygame.math.Vector2(*pops)
    follower_vector = pygame.math.Vector2(*fpos)
    new_follower_vector = pygame.math.Vector2(*fpos)

    distance = follower_vector.distance_to(target_vector)
    if distance > minimum_distance:
        direction_vector = (target_vector - follower_vector) / distance
        min_step = max(0, distance - maximum_distance)
        max_step = distance - minimum_distance
        step_distance = min_step + (max_step - min_step) * LERP_FACTOR
        new_follower_vector = follower_vector + direction_vector * step_distance

    return new_follower_vector


def update(events, delta_time):
    update_keys(events)
    player.update(events, delta_time)


def draw():
    screen.fill(pygame.color.Color(34, 35, 35))
    player.draw(screen)


while running:
    delta_time = clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    update(events, delta_time)
    dog = FollowMe(player.pos, dog)
    draw()
    if dog.x < player.pos.x:
        screen.blit(pygame.transform.flip(dog_tile, True, False), dog)
    else:
        screen.blit(dog_tile, dog)

    pygame.display.flip()

pygame.quit()
