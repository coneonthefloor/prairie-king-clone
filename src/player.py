import os
import pygame
from constants import FLOOR, GRAVITY
from game_object import GameObject
from tilemap import Tilemap


class Animation:
    def __init__(self, frames: list[pygame.Surface], frame_rate: int) -> None:
        self.frames = frames
        self.frame_rate = frame_rate
        self.current_frame_index = 0
        self.last_tick = pygame.time.get_ticks()

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_tick >= self.frame_rate:
            self.last_tick = current_time
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

    def enter(self):
        self.current_frame_index = 0
        self.last_tick = pygame.time.get_ticks()

    def exit(self):
        self.current_frame_index = 0

    def get_current_frame(self) -> pygame.Surface:
        return self.frames[self.current_frame_index]


class Player(GameObject):
    def __init__(self):
        super().__init__("player")
        tile_sheet = pygame.image.load(os.path.join("assets", "characters.png"))
        tilemap = Tilemap(tile_sheet, (32, 32), 0, 0)
        tilemap.load()

        self.sprite_scale = (3, 3)

        self.running_frames = [
            tilemap.get_tile_scaled((i, 1), self.sprite_scale) for i in range(14, 18)
        ]
        self.running_animation = Animation(self.running_frames, 100)
        self.running = True

        self.jumping_frames = [
            tilemap.get_tile_scaled((i, 1), self.sprite_scale) for i in range(5, 8)
        ]
        self.jumping_animation = Animation(self.jumping_frames, 700)
        self.jumping = False

        self.speed = 4
        self.jump_force = 20
        self.vel = pygame.math.Vector2()
        self.height = self.running_animation.get_current_frame().get_height()
        self.width = self.running_animation.get_current_frame().get_width()
        self.initial_pos = pygame.math.Vector2(50, FLOOR - self.height)
        self.pos = self.initial_pos.copy()

    def bottom(self) -> int:
        return self.pos.y + self.height

    def jump(self):
        if self.bottom() == FLOOR and not self.jumping:
            self.vel.y -= self.jump_force
            self.running = False
            self.running_animation.exit()
            self.jumping = True
            self.jumping_animation.enter()

    def update(self):
        if self.jumping:
            self.jumping_animation.update()

        if self.running:
            self.running_animation.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.jump()

        if self.jumping:
            self.vel.y += GRAVITY

        self.pos += self.vel

        if self.bottom() > FLOOR:
            self.pos.y = FLOOR - self.height
            self.vel.y = 0
            self.jumping = False
            self.jumping_animation.exit()
            self.running = True
            self.running_animation.enter()

    def draw(self, surface):
        if self.jumping:
            surface.blit(self.jumping_animation.get_current_frame(), self.pos)

        if self.running:
            surface.blit(self.running_animation.get_current_frame(), self.pos)
