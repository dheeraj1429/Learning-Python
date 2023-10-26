import pygame
import sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 432

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
scroll = 0

# background images list
bg_image_list = []
for i in range(1, 6):
    new_image_surface = pygame.image.load(f'.//graphics/plx-{i}.png').convert_alpha()
    bg_image_list.append(new_image_surface)
first_bg_width = bg_image_list[0].get_width()


def draw_bg():
    for tile in range(5):
        bg_speed = 0
        for background_image in bg_image_list:
            display_surface.blit(background_image, (tile * first_bg_width - scroll * bg_speed, 0))
            bg_speed += 0.2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        scroll += 10
    if keys[pygame.K_LEFT]:
        scroll -= 10

    # delta time
    dt = clock.tick(60) / 1000

    draw_bg()

    # update frame.
    pygame.display.update()
