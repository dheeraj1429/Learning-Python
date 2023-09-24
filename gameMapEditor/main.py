import pygame
from settings import *
from sys import exit
from utils import load_folder
from button import Button

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HIGHT + LOWER_MARGIN))
        self.scroll = 0
        self.scroll_left = False
        self.scroll_right = False
        self.bg_image = pygame.image.load('./public/background/4173391.png').convert_alpha()
        self.menu_images = load_folder('./public/graphics/menu')
        self.drawer_row = 0
        self.drawer_column = 0
        self.menu_buttons = self.load_menu_buttons(self.menu_images)
        self.current_menu_item = 0
        
    def load_menu_buttons(self, menu_images):
        menu_button_list = []
        for item in menu_images:
            x = SCREEN_WIDTH + (75 * self.drawer_column + 50)
            y = 75 * self.drawer_row + 50
            new_button = Button(item, x, y, 1)
            menu_button_list.append(new_button)
            self.drawer_column += 1
            if self.drawer_column >= 3:
                self.drawer_row += 1
                self.drawer_column = 0
            
        return menu_button_list
        
    def drawer(self):
        pygame.draw.rect(self.screen, GRAY, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HIGHT + LOWER_MARGIN))
        pygame.draw.rect(self.screen, GRAY, (0, SCREEN_HIGHT, SCREEN_WIDTH, LOWER_MARGIN))

    def draw_background(self):
        bg_width = self.bg_image.get_width()
        for x in range(6):
            self.screen.blit(self.bg_image, (x * bg_width - self.scroll, 0))

    def draw_grid(self):
        for col in range(MAX_COLS + 1):
            x = col * TILE_SIZE - self.scroll
            pygame.draw.line(self.screen, MAIN_COLOR, (x, 0), (x, SCREEN_WIDTH))
        for row in range(ROWS + 1):
            y = row * TILE_SIZE
            pygame.draw.line(self.screen, MAIN_COLOR, (0, y), (SCREEN_WIDTH, y))
            
    def draw_menu(self):
        for button in range(len(self.menu_buttons)):
            if self.menu_buttons[button].draw(self.screen):
                self.current_menu_item = button
            
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                # keep track the key events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.scroll_left = True
                    if event.key == pygame.K_RIGHT:
                        self.scroll_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.scroll_left = False
                    if event.key == pygame.K_RIGHT:
                        self.scroll_right = False
                        
            if self.scroll_left and self.scroll > 0:
                self.scroll -= 5
            elif self.scroll_right and self.scroll < self.bg_image.get_width() * 4:
                self.scroll += 5
            
            self.screen.fill('white')
            self.draw_background()
            self.draw_grid()
            self.drawer()
            self.draw_menu()
            pygame.draw.rect(self.screen, BLACK, self.menu_buttons[self.current_menu_item].rect, 2)
            pygame.display.update()
    
if __name__ == '__main__':
    main = Main()
    main.run()