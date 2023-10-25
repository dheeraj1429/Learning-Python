import pygame
from utils import import_folder
from settings import GROUND_POSITION_Y


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups, collision_sprite):
        super().__init__(groups)
        self.collision_sprite = collision_sprite
        self.collision_detected = False
        self.initial_position = initial_position
        self.reset_game = False

        # frames
        self.frames = import_folder('../graphics/player/run')
        self.animation_frame_index = 0
        self.image = self.frames[self.animation_frame_index]
        self.rect = self.image.get_rect(center=(self.initial_position))

        # sounds
        self.jump_sound = pygame.mixer.Sound('../sound/jump.wav')
        self.die_sound = pygame.mixer.Sound('../sound/die.wav')
        self.score_sound = pygame.mixer.Sound('../sound/point.wav')

        # float base movement
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 200
        self.can_jump = False
        self.can_run = False
        self.start_run = False

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
            if self.can_run and not self.start_run:
                self.start_run = True

    def animation(self):
        if self.can_run and self.start_run and not self.collision_detected:
            self.animation_frame_index += 0.3
            if self.animation_frame_index > len(self.frames):
                self.animation_frame_index = 0
            self.image = self.frames[int(self.animation_frame_index)]

    def run(self, dt):
        if self.start_run and not self.collision_detected:
            self.rect.x += self.direction.x * self.speed * dt

    def jump(self):
        self.animation_frame_index = 0
        self.image = self.frames[self.animation_frame_index]
        self.can_jump = False
        self.gravity = -self.gravity_offset
        self.can_run = True
        self.jump_sound.play()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_jump and not self.collision_detected:
            self.jump()

        if keys[pygame.K_r] and self.collision_detected:
            self.reset()

    def collision(self):
        if pygame.sprite.spritecollide(self, self.collision_sprite, False, pygame.sprite.collide_mask) and not self.collision_detected:
            self.start_run = False
            self.collision_detected = True
            self.image = pygame.image.load('../graphics/player/game_over_light.png').convert_alpha()
            self.die_sound.play()
            self.reset_game = False

    def reset(self):
        self.reset_game = True
        self.collision_detected = False
        self.jump()

    def update(self, dt):
        self.input()
        self.apply_gravity(dt)
        self.collision()
        # self.run(dt)
