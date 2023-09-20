import pygame
from settings import screen_height, screen_width
from sys import exit
from level import Level
from game_data import level_0

# set up
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# level initialization
level = Level(level_data=level_0, surface=screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    screen.fill('gray')
    clock.tick(60)
    level.run()
