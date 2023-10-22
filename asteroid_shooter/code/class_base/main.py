import pygame
import sys
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
window_half_pos = WINDOW_WIDTH / 2
ship_y_pos = WINDOW_HEIGHT - 120
can_shoot = True
shoot_time = None

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid shooter')
clock = pygame.time.Clock()


game_background_surface = pygame.image.load('../../graphics/background.png').convert_alpha()
font = pygame.font.Font('../../graphics/subatomic.ttf', size=50)


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, direction, pos):
        super().__init__(groups)
        self.image = pygame.image.load('../../graphics/meteor.png').convert_alpha()
        self.meteor_size = pygame.math.Vector2(self.image.get_size()) * random.uniform(0.5, 1.5)
        self.image = pygame.transform.scale(self.image, self.meteor_size)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.speed = 200
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

        if self.rect.bottom > WINDOW_HEIGHT + 100:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load('../../graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 800
        self.direction = pygame.math.Vector2(0, -1)
        self.explosion_sound = pygame.mixer.Sound('../../sounds/explosion.wav')
        self.explosion_sound.set_volume(.04)
        self.mask = pygame.mask.from_surface(self.image)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_sprite_group, True, pygame.sprite.collide_mask):
            self.explosion_sound.play()
            self.kill()

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collision()

        if self.rect.y < 0:
            self.kill()


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../../graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(window_half_pos, ship_y_pos))
        self.can_shoot = True
        self.shoot_time = None
        self.laser_sound = pygame.mixer.Sound('../../sounds/laser.ogg')
        self.laser_sound.set_volume(.3)
        self.mask = pygame.mask.from_surface(self.image)

    def input(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_timer(self, duration=300):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > duration:
                self.can_shoot = True

    def shoot_laser(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            Laser(sprite_group, self.rect.midtop)
            self.laser_sound.play()

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_sprite_group, False, pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()

    def update(self, dt):
        self.input()
        self.shoot_laser()
        self.laser_timer()
        self.meteor_collision()


# sprite groups
sprite_group = pygame.sprite.Group()
meteor_sprite_group = pygame.sprite.Group()

ship = Ship(sprite_group)

# game timers
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # timer events
        if event.type == meteor_timer:
            meteor_direction = pygame.math.Vector2((random.uniform(-0.5, .5)), 1)
            meteor_pos = (random.randint(0, WINDOW_WIDTH), -100)
            meteor = Meteor(meteor_sprite_group, meteor_direction, meteor_pos)

    # delta time
    dt = clock.tick(60) / 1000

    # update
    sprite_group.update(dt)
    meteor_sprite_group.update(dt)

    # background
    display_surface.blit(game_background_surface, (0, 0))
    sprite_group.draw(display_surface)
    meteor_sprite_group.draw(display_surface)

    # update the window
    pygame.display.update()
