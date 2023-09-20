import pygame
from utils import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_size, x, y):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, tile_size, x, y, surface):
        super().__init__(tile_size, x, y)
        self.image = surface


class Crate(StaticTile):
    def __init__(self, tile_size, x, y):
        super().__init__(tile_size, x, y, pygame.image.load(
            '../public/graphics/terrain/crate.png').convert_alpha())
        offset_y = y + tile_size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))


class AnimatedTile(Tile):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift


class Coin(AnimatedTile):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y, path)
        self.center_x = x + int(tile_size / 2)
        self.center_y = y + int(tile_size / 2)
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))


class Plam(AnimatedTile):
    def __init__(self, tile_size, x, y, path, offset_y):
        super().__init__(tile_size, x, y, path)
        offset_y = y - offset_y
        self.rect.topleft = (x, offset_y)
