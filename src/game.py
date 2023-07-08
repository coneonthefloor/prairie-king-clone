import os
import pygame
from custom_cursor import CustomCursor
from tile_defs import TileDefs
from tilemap import Tilemap

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
goblin_image_squash = tilemap.get_tile_scaled(TileDefs.GOBLIN, (6.5, 6))
goblin_image_squeeze = tilemap.get_tile_scaled(TileDefs.GOBLIN, (6, 6.5))
goblin_image = goblin_image_original
goblin_rect = goblin_image.get_rect()
goblin_anim_frame = 0
goblin_max_anim_frame = 1
goblin_rect.center = pygame.math.Vector2(
    screen.get_width() // 2, screen.get_height() // 2
)
goblin_speed = 4
goblin_dest = None
goblin_anim_speed = 0.33
goblin_anim_start = pygame.time.get_ticks()


def move_towards(origin, dest, speed):
    return pygame.math.Vector2(*origin).move_towards(dest, speed)


def distance_to(origin, dest):
    return pygame.math.Vector2(*origin).distance_to(dest)


class GameObject:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()

    def get_image_height(self):
        return self.image.get_height()

    def get_image_width(self):
        return self.image.get_width()

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed

        if self.pos.left >= WIDTH:
            self.pos.right = self.speed
        if self.pos.right <= 0:
            self.pos.left = WIDTH - self.speed

        if self.pos.top >= HEIGHT:
            self.pos.bottom = self.speed
        if self.pos.bottom <= 0:
            self.pos.top = HEIGHT - self.speed


p = GameObject(goblin_image, goblin_speed)

while RUNNING:
    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)

    screen.fill((34, 35, 35))

    goblin_pos_rounded = (round(goblin_rect.x), round(goblin_rect.y))
    screen.blit(goblin_image, goblin_pos_rounded)

    screen.blit(p.image, p.pos)

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
                goblin_image = goblin_image_squash
            if goblin_anim_frame == 1:
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
