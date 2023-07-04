import pygame

from component import Component
from keyboard import is_key_down


class PlayerMovement(Component):
    def __init__(self, player):
        super().__init__("PlayerMovement")
        self.player = player

    def process_events(self, events):
        up_pressed = is_key_down(pygame.K_UP)
        down_pressed = is_key_down(pygame.K_DOWN)
        left_pressed = is_key_down(pygame.K_LEFT)
        right_pressed = is_key_down(pygame.K_RIGHT)

        if up_pressed and not down_pressed:
            self.player.vel.y = -1
        if down_pressed and not up_pressed:
            self.player.vel.y = 1
        if not up_pressed and not down_pressed:
            self.player.vel.y = 0

        if left_pressed and not right_pressed:
            self.player.vel.x = -1
        if right_pressed and not left_pressed:
            self.player.vel.x = 1
        if not left_pressed and not right_pressed:
            self.player.vel.x = 0

    def update(self, events, delta_time):
        self.process_events(events)
