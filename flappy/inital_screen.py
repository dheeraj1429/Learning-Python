import pygame

class InitalScreen(pygame):
    def __init__(self):
        super().__init__()
        self.game_font = pygame.font.Font('./assets/font/FlappybirdyRegular-KaBW.ttf', 100)
        self.game_heading = self.game_font.render('Flappy Bird', False, "White")
        self.game_heading_rect = self.game_heading.get_rect(center=(250, 200))
    
    def get_game_heading(self):
        return self.game_heading

    def get_game_heading_rect(self):
        return self.game_heading_rect