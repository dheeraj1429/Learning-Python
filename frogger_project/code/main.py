import pygame
import sys
import random
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, CAR_START_POSITIONS, SIMPLE_OBJECTS, LONG_OBJECTS
from player import Player
from car import Car
from obstacle import Obstacle

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger Game")
clock = pygame.time.Clock()


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load('../graphics/main/map.png').convert_alpha()
        self.fg = pygame.image.load('../graphics/main/overlay.png').convert_alpha()

    def customize_draw(self):
        # change the offset.
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # blit the background
        display_surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda item: item.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, -self.offset)


# sprite groups
all_sprite_groups = AllSprites()
obstacle_sprite = pygame.sprite.Group()

# objects initialization
player = Player((2062, 3247), all_sprite_groups, obstacle_sprite)

# timers
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 70)
pos_list = []

# obstacles setup
simple_obstacle_path = '../graphics/objects/simple'
long_obstacle_path = '../graphics/objects/long'


def create_obstacles(obstacle, path):
    for (file_name, position_list) in obstacle.items():
        obstacle_surface = pygame.image.load(f'{path}/{file_name}.png').convert_alpha()
        for position in position_list:
            Obstacle(surface=obstacle_surface, initial_position=position, groups=[all_sprite_groups, obstacle_sprite])


create_obstacles(SIMPLE_OBJECTS, simple_obstacle_path)
create_obstacles(LONG_OBJECTS, long_obstacle_path)

while True:
    # event loop
    for event in pygame.event.get():

        # exit event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # timer events
        if event.type == car_timer:
            random_car_position = random.choice(CAR_START_POSITIONS)
            if not random_car_position in pos_list:
                pos_list.append(random_car_position)
                Car((random_car_position[0], random_car_position[1] + random.randint(-8, 8)), all_sprite_groups)

            if len(pos_list) > 5:
                del pos_list[0]

    # delta time
    dt = clock.tick(60) / 1000

    display_surface.fill('black')
    # draw sprite
    all_sprite_groups.customize_draw()

    # update the display surface and drawing the frames
    all_sprite_groups.update(dt)
    pygame.display.update()
