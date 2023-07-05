import pygame
from entity import Entity
from tile_defs import TileDefs


class Cursor(Entity):
    def __init__(self, tilemap, scale):
        super().__init__("Cursor")
        self.scale = scale
        self.position = (0, 0)
        self.diagonal = tilemap.get_tile_scaled(TileDefs.DIAGONAL_CROSSHAIR, scale)
        self.diagonal_clicked = tilemap.get_tile_scaled(
            TileDefs.DIAGONAL_CROSSHAIR_CLICKED, scale
        )
        self.current_image = self.diagonal

    def update(self, events, delta_time):
        super().update(events, delta_time)
        self.position = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.current_image = self.diagonal_clicked
        else:
            self.current_image = self.diagonal

    def draw(self, surface):
        surface.blit(self.current_image, self.position)
