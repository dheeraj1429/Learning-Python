import pygame
import sys
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, GROUND_POSITION_X, GROUND_POSITION_Y, GROUND_WIDTH
from player import Player
from ground import Ground

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()

ground_count = 0

# sprite groups
all_sprite_groups = pygame.sprite.Group()

# sprite initialization
player = Player((100, 100),  all_sprite_groups)
Ground(groups=all_sprite_groups, initial_position=(GROUND_POSITION_X + ground_count * GROUND_WIDTH, GROUND_POSITION_Y))

# timers
game_ground_timer = pygame.event.custom_type()
pygame.time.set_timer(game_ground_timer, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == game_ground_timer:
            ground_count += 1
            new_ground = Ground(groups=all_sprite_groups, initial_position=(GROUND_POSITION_X + ground_count * GROUND_WIDTH, GROUND_POSITION_Y))

    # delta time
    dt = clock.tick(60) / 1000

    # drawing sprites
    all_sprite_groups.draw(display_surface)

    pygame.display.update()
    all_sprite_groups.update(dt)
    display_surface.fill((255, 255, 255))
