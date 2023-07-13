import pygame


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