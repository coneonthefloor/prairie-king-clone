import os
import pygame
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


class CustomCursor:
    def __init__(self, default_image, clicked_image):
        self.default_image = default_image
        self.clicked_image = clicked_image

    def draw(self, surface):
        surface.blit(self.get_image(), pygame.mouse.get_pos())

    def get_image(self):
        if self.mouse_pressed():
            return self.clicked_image
        return self.default_image

    def mouse_pressed(self):
        return pygame.mouse.get_pressed()[0]


cursor = CustomCursor(
    tilemap.get_tile_scaled(TileDefs.DIAGONAL_CROSSHAIR, (4, 4)),
    tilemap.get_tile_scaled(TileDefs.DIAGONAL_CROSSHAIR_CLICKED, (4, 4)),
)


while RUNNING:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False

    update_keys(events)

    screen.fill((34, 35, 35))

    cursor.draw(screen)

    pygame.display.flip()

pygame.quit()
