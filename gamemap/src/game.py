import pygame
from settings import screen_width, screen_height
from sys import exit
from level import Level
from game_data import level_0

# Screen initialization
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Level initialization
level = Level(level_data=level_0, surface=screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('white')
    level.run()

    pygame.display.update()
    clock.tick(60)
