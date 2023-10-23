import pygame
import random
from os import walk
from settings import WINDOW_WIDTH


class Car(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups):
        super().__init__(groups)
        self.image = None
        self.random_car()
        self.rect = self.image.get_rect(center=initial_position)

        # float base movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 300

        if initial_position[0] < 200:
            self.direction = pygame.math.Vector2(1, 0)
        else:
            self.direction = pygame.math.Vector2(-1, 0)
            self.image = pygame.transform.flip(self.image, True, False)

    def random_car(self):
        path = '../graphics/cars'
        cars_list = walk(path)
        for (_, _2, folder) in cars_list:
            random_car = random.choice(folder)
            self.image = pygame.image.load(f'{path}/{random_car}').convert_alpha()

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def update(self, dt):
        self.move(dt)

        if not -200 < self.rect.x < WINDOW_WIDTH + 100:
            self.kill()
