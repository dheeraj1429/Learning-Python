import pygame
import sys
from settings import WINDOW_HEIGHT, WINDOW_WIDTH
from player import Player
from car import Car

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger Game")
clock = pygame.time.Clock()


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2(0, -100)
        self.bg = pygame.image.load('../graphics/main/map.png').convert_alpha()
        self.fg = pygame.image.load('../graphics/main/overlay.png').convert_alpha()

    def customize_draw(self):
        display_surface.blit(self.bg, self.offset)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, self.offset)


# sprite groups
all_sprite_groups = AllSprites()

# objects initialization
player = Player((500, 400), all_sprite_groups)
car = Car((400, 200), all_sprite_groups)

while True:
    # event loop
    for event in pygame.event.get():

        # exit event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick(60) / 1000

    display_surface.fill('black')
    # draw sprite
    all_sprite_groups.customize_draw()

    # update the display surface and drawing the frames
    all_sprite_groups.update(dt)
    pygame.display.update()
