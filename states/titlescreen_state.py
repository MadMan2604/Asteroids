# the title screen script
## loads an interactive title screen that shows a play button, options button, and a quit button
### the options button will change the screen to a options screen where the user can change their graphics, screen dimentions, and audio preferences

import pygame 
import sys 
import pygame_menu

from pygame.locals import *
from pygame_menu.widgets import *
from scripts.settings import * 
from states.main_state import InGame
from scripts.buttons import Button
from states.base_state import BaseState

# TITLE SCREEN CLASS
class Title_Screen(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen 
        self.button = Button()


    
    # CREATES THE TITLE SCREEN
    def title_screen(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(pygame.mouse.get_pos()):
                        InGame().main_game()
                    elif options_button.collidepoint(pygame.mouse.get_pos()):
                        print('Options Screen')
                    elif instructions_button.collidepoint(pygame.mouse.get_pos()):
                        print('Instructions Screen')
                    elif quit_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
            
            self.screen.fill(BLACK)

            # DRAW THE TITLE SCREEN BACKGROUND
            title_screen_bg = pygame.image.load(TITLE_SCREEN_IMG)
            title_screen_bg = pygame.transform.scale(title_screen_bg, (WIDTH, HEIGHT))
            self.screen.blit(title_screen_bg, (0, 0))

            # DRAW THE TITLE SCREEN NAME
            title_screen_text = self.font2.render("ASTEROIDS", True, WHITE)
            self.screen.blit(title_screen_text, (375, 200))

            # DRAW THE BUTTONS
            play_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Play", WHITE, self.font1, BLACK)
            options_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
            instructions_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Instructions", WHITE, self.font1, BLACK)
            quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)

            

            
            pygame.display.flip()
            self.clock.tick(FPS)


                