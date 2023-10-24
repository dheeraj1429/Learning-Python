import pygame
import sys
import random


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
display_surface = pygame.display.set_mode((screen_width, screen_height))

moving_rect = pygame.Rect(random.randint(0, screen_width - 200), random.randint(0, screen_height - 200), 100, 100)
moving_rect_speed_x, moving_rect_speed_y = 5, 4

other_rect = pygame.Rect(random.randint(0, screen_width - 300), random.randint(0, screen_height - 300),  100, 20)
other_rect_y_speed = 4


def bounce_rect():
    global moving_rect_speed_x, moving_rect_speed_y, other_rect_y_speed
    moving_rect.x += moving_rect_speed_x
    moving_rect.y += moving_rect_speed_y
    other_rect.y += other_rect_y_speed

    # collision detection with screen border
    if moving_rect.right >= screen_height or moving_rect.left <= 0:
        moving_rect_speed_x *= -1
    if moving_rect.top <= 0 or moving_rect.bottom >= screen_height:
        moving_rect_speed_y *= -1

    if other_rect.bottom >= screen_height or other_rect.top <= 0:
        other_rect_y_speed *= -1

    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and moving_rect_speed_y > 0:
            moving_rect_speed_y *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and moving_rect_speed_y < 0:
            moving_rect_speed_y *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and moving_rect_speed_x > 0:
            moving_rect_speed_x *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and moving_rect_speed_x < 0:
            moving_rect_speed_x *= -1

    pygame.draw.rect(display_surface, (255, 255, 255), moving_rect)
    pygame.draw.rect(display_surface, (255, 0, 0), other_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60) / 1000

    # draw
    display_surface.fill((30, 30, 30))
    bounce_rect()

    pygame.display.update()
