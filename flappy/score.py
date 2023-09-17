import pygame

class Score():
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font('./assets/font/Blomberg-8MKKZ.otf', 20)
        self.start_time = 0
        self.heading = self.font.render("Score: 0", False, 'White')
        self.rect = self.heading.get_rect(center=(250, 50))
        
    def update_score(self):
        self.score = pygame.time.get_ticks() - self.start_time
        self.heading = self.font.render(f"Score: {int(self.score / 1000)}", False, 'White')
        return self.score