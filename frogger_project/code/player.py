import pygame
from os import walk
from utils.utils import import_folders


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups):
        super().__init__(groups)
        self.initial_position = initial_position

        # animation list
        self.animations = {}
        self.animation_frame_index = 0
        self.move_direction = 'right'
        self.import_assets()
        self.image = self.animations[self.move_direction][self.animation_frame_index]
        self.rect = self.image.get_rect(center=(self.initial_position))

        # float base movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200

    def collision(self):
        pass

    def import_assets(self):
        for (index, folder) in enumerate(walk('../graphics/player')):
            if index == 0:
                for (folder_name) in folder[1]:
                    self.animations[folder_name] = []
            else:
                replace_path = folder[0].replace("\\", '/')
                original_path = replace_path.split('/')[-1]
                self.animations[original_path] = import_folders(folder[0])

    def frame_animation(self, dt):
        if self.direction.magnitude():
            self.animation_frame_index += 10 * dt
            if self.animation_frame_index >= len(self.animations[self.move_direction]):
                self.animation_frame_index = 0
        else:
            self.animation_frame_index = 0
        self.image = self.animations[self.move_direction][int(self.animation_frame_index)]

    def move(self, dt):
        # normalize movement vector
        if self.direction.magnitude():
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def input(self, dt):
        keys = pygame.key.get_pressed()

        # horizontal movements
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.move_direction = 'right'
            self.frame_animation(dt)
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.move_direction = 'left'
            self.frame_animation(dt)
        else:
            self.direction.x = 0

        # vertical movements
        if keys[pygame.K_UP]:
            self.move_direction = 'up'
            self.frame_animation(dt)
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.move_direction = 'down'
            self.frame_animation(dt)
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self, dt):
        self.input(dt)
        self.move(dt)
        self.collision()
