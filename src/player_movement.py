import math
import pygame

from component import Component
from keyboard import is_key_down


class PlayerMovement(Component):
    def __init__(self, player):
        super().__init__("PlayerMovement")
        self.player = player

    def process_events(self, events):
        if is_key_down(pygame.K_LEFT):
            self.player.vel.x = -self.player.speed
        if is_key_down(pygame.K_RIGHT):
            self.player.vel.x = self.player.speed
        if is_key_down(pygame.K_UP):
            self.player.vel.y = -self.player.speed
        if is_key_down(pygame.K_DOWN):
            self.player.vel.y = self.player.speed

    def update(self, events, delta_time):
        self.process_events(events)

        x, y = self.player.vel
        speed = math.sqrt(x * x + y * y)
        angle = math.atan2(y, x)

        if speed > self.player.friction:
            speed -= self.player.friction
        else:
            speed = 0

        self.player.vel.x = math.cos(angle) * speed
        self.player.vel.y = math.sin(angle) * speed
