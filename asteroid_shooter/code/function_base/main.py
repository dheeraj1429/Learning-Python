import random
import pygame
from sys import exit
pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
window_half_pos = WINDOW_WIDTH / 2
ship_y_pos = WINDOW_HEIGHT - 120
can_shoot = True
shoot_time = None

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid shooter')

game_background_surface = pygame.image.load(
    '../graphics/background.png').convert_alpha()
font = pygame.font.Font('../graphics/subatomic.ttf', size=50)

text_surface = font.render('Space', True, 'white')
text_rect = text_surface.get_rect(center=(WINDOW_WIDTH / 2, 120))
clock = pygame.time.Clock()


# ship
ship_surface = pygame.image.load('../graphics/ship.png').convert_alpha()
ship_rect = ship_surface.get_rect(center=(window_half_pos, ship_y_pos))

# metero
meteor_surface = pygame.image.load('../graphics/meteor.png').convert_alpha()
meteor_list = []

# laser
laser_surface = pygame.image.load('../graphics/laser.png').convert_alpha()
laser_list = []

# sounds
laser_sound = pygame.mixer.Sound('../sounds/laser.ogg')
laser_sound.set_volume(.3)
explosion_sound = pygame.mixer.Sound('../sounds/explosion.wav')
explosion_sound.set_volume(.08)
game_sound = pygame.mixer.Sound('../sounds/music.wav')
game_sound.set_volume(0.2)
game_sound.play()

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 200)


def laser_shoot(can_shoot, duration=300):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and can_shoot:
                laser_list.append(laser_surface.get_rect(
                    midbottom=ship_rect.midtop))
                laser_sound.play()

            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
            meteor_rect = meteor_surface.get_rect(
                center=(random.randint(0, WINDOW_WIDTH), -100))
            diraction = pygame.math.Vector2(random.uniform(-0.8, 0.8), 1)
            meteor_list.append((meteor_rect, diraction))

    delta_time = clock.tick(60) / 1000
    ship_rect.center = pygame.mouse.get_pos()

    display_surface.blit(game_background_surface, (0, 0))
    display_surface.blit(text_surface, text_rect)

    pygame.draw.rect(display_surface, 'red', text_rect.inflate(
        30, 30), border_radius=8, width=5)

    for laser_rect in laser_list:
        # check the meteor and laser collection.
        for (meteor_rect, diraction) in meteor_list:
            if (laser_rect.colliderect(meteor_rect)):
                explosion_sound.play()
                meteor_list.remove((meteor_rect, diraction))

        display_surface.blit(laser_surface, laser_rect)
        laser_rect.y -= round(600 * delta_time)
        if laser_rect.y < -50:
            laser_list.remove(laser_rect)

    display_surface.blit(ship_surface, ship_rect)

    for (meteor_rect, diraction) in meteor_list:
        # ship and meteor collection.
        if (ship_rect.colliderect(meteor_rect)):
            pygame.quit()
            exit()

        meteor_rect.center += diraction * round(300 * delta_time)
        display_surface.blit(meteor_surface, meteor_rect)

        if meteor_rect.bottom > WINDOW_HEIGHT + 200:
            meteor_list.remove((meteor_rect, diraction))

    pygame.display.update()
    can_shoot = laser_shoot(can_shoot, 200)
