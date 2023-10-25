import pygame
import sys
import random
from player import Player
from ground import Ground
from obstacle import Obstacle
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, GROUND_POSITION_X, GROUND_POSITION_Y, GROUND_WIDTH


pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()
ground_count = 0


class AllSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

    def custom_draw(self):
        # self.offset.x = player.rect.centerx - GROUND_POSITION_X - 100
        for sprite in self.sprites():
            # offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, sprite.rect)
            if player.start_run and not player.collision_detected:
                sprite.can_move = True
            else:
                sprite.can_move = False

            if player.reset_game:
                if sprite.__class__.__name__ == 'Obstacle':
                    sprite.kill()


# sprite groups
# player_sprite_group = pygame.sprite.GroupSingle()
# ground_sprite_group = pygame.sprite.GroupSingle()
obstacle_sprite_group = pygame.sprite.Group()
all_sprite_groups = AllSprite()


# sprite initialization
player = Player((100, 100),  all_sprite_groups, obstacle_sprite_group)
Ground(groups=all_sprite_groups, initial_position=(GROUND_POSITION_X + ground_count * GROUND_WIDTH, GROUND_POSITION_Y))

# timers
game_ground_timer = pygame.event.custom_type()
obstacle_timer = pygame.event.custom_type() + 1
restart_timer = pygame.event.custom_type() + 2

pygame.time.set_timer(game_ground_timer, 500)
pygame.time.set_timer(obstacle_timer, 1000)
pygame.time.set_timer(restart_timer, 1000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == game_ground_timer:
            if player.start_run:
                ground_count += 1
                ground_x_pos = ground_count * GROUND_WIDTH + 200
                new_ground = Ground(groups=all_sprite_groups, initial_position=(ground_x_pos, GROUND_POSITION_Y))

        if event.type == obstacle_timer:
            if player.start_run:
                Obstacle(initial_position=(random.randint(WINDOW_WIDTH + 100, WINDOW_WIDTH + 500), GROUND_POSITION_Y + 20), groups=[all_sprite_groups, obstacle_sprite_group])

        if event.type == restart_timer:
            if player.reset_game:
                player.reset_game = False

    # delta time
    dt = clock.tick(60) / 1000

    # display color
    display_surface.fill((255, 255, 255))

    # drawing sprites
    all_sprite_groups.custom_draw()

    # update
    all_sprite_groups.update(dt)
    pygame.display.update()
