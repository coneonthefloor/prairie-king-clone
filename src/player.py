import math
import pygame

from entity import Entity
from player_movement import PlayerMovement


class Player(Entity):
    def __init__(self):
        super().__init__("Player")
        self.pos = pygame.math.Vector2()
        self.vel = pygame.math.Vector2()
        self.speed = 0.5
        self.friction = 0.25
        self.add_component(PlayerMovement(self))

    def update(self, events, delta_time):
        super().update(events, delta_time)
        self.pos = self.pos + self.vel * delta_time
