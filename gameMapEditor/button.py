import pygame

class Button:
    def __init__(self, image, x, y, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action =  False
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
            if pygame.mouse.get_pressed()[0]:
                action = True
                self.clicked = True
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action