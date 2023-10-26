import pygame
import sys

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# game sprites
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

# ----------------------------------------------------------------


class StaticObstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()


class MovingVerticalObstacle(StaticObstacle):
    def __init__(self, pos, size, groups, color):
        super().__init__(pos, size, groups)
        self.image.fill(color)
        self.direction = pygame.math.Vector2((0, 1))
        self.speed = 500

    def update(self, dt):
        self.old_rect = self.rect.copy()
        if self.rect.y >= WINDOW_HEIGHT - (self.image.get_size()[1] + 20):
            self.direction.y *= -1
        if self.rect.y <= 10:
            self.direction.y *= -1
        self.rect.y += self.direction.y * self.speed * dt


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, obstacles):
        super().__init__(groups)

        # image
        self.image = pygame.Surface((30, 60))
        self.image.fill('blue')

        # position
        self.rect = self.image.get_rect(topleft=(640, 360))
        self.old_rect = self.rect.copy()

        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.obstacles = obstacles

    def collision(self):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)
        if collision_sprites:
            for sprite in collision_sprites:
                if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                    self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x

                if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                    self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x

                if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y

                if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                    self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y

    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.topleft = self.pos
        self.collision()


StaticObstacle((800, 600), (100, 200), [all_sprites, collision_sprites])
StaticObstacle((900, 200), (200, 100), [all_sprites, collision_sprites])
StaticObstacle((200, 400), (200, 100), [all_sprites, collision_sprites])
MovingVerticalObstacle((500, 500), (100, 30), [all_sprites, collision_sprites], color='pink')
Player(all_sprites, collision_sprites)

# ----------------------------------------------------------------


# clock
clock = pygame.time.Clock()

while True:

    # delta time
    dt = clock.tick(60) / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing and updating the screen
    screen.fill('black')
    all_sprites.update(dt)
    all_sprites.draw(screen)

    # display output
    pygame.display.update()
