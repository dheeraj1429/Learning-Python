import pygame
from utils import import_folder
from settings import GROUND_POSITION_Y


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups):
        super().__init__(groups)

        # frames
        self.frames = import_folder('../graphics/player/run')
        self.animation_frame_index = 0
        self.image = self.frames[self.animation_frame_index]
        self.rect = self.image.get_rect(center=(initial_position))

        # float base movement
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 200
        self.can_jump = False

        # gravity
        self.gravity = 0
        self.gravity_offset = 20

    def apply_gravity(self, dt):
        self.gravity += 70 * dt
        self.rect.y += self.gravity
        if self.rect.bottom >= GROUND_POSITION_Y + self.gravity_offset:
            self.rect.bottom = GROUND_POSITION_Y + self.gravity_offset
            self.can_jump = True
            self.animation()

    def animation(self):
        self.animation_frame_index += 0.3
        if self.animation_frame_index > len(self.frames):
            self.animation_frame_index = 0
        self.image = self.frames[int(self.animation_frame_index)]

    def run(self, dt):
        self.rect.x += self.direction.x * self.speed * dt

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_jump:
            self.animation_frame_index = 0
            self.image = self.frames[self.animation_frame_index]
            self.can_jump = False
            self.gravity = -self.gravity_offset

    def update(self, dt):
        self.input()
        self.apply_gravity(dt)
