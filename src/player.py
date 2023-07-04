import pygame

from entity import Entity
from player_movement import PlayerMovement


class Player(Entity):
    def __init__(self, image):
        super().__init__("Player")
        self.speed = 0.2
        self.image = image
        self.pos = pygame.math.Vector2()
        self.vel = pygame.math.Vector2()
        self.rect = self.image.get_rect(center=self.get_center())
        self.add_component(PlayerMovement(self))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, events, delta_time):
        super().update(events, delta_time)
        if self.vel.x and self.vel.y:
            self.vel = self.vel.normalize()
        self.pos = self.pos + self.vel * self.speed * delta_time
        self.rect.center = self.get_center()

    def get_center(self):
        return (round(self.pos.x), round(self.pos.y))
