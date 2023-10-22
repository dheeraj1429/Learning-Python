import pygame


class Timer:
    def __init__(self, duration, function=None):
        self.duration = duration
        self.function = function
        self.active = False
        self.start_time = 0

    def activate(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            print('de activate the timer..')