# GAME OVER SCREEN STATE 
import pygame
import sys
import os 
import math 

from scripts.settings import *
from scripts.buttons import Button
from states.base_state import BaseState
#from scripts.title import Title_Screen

# GAME OVER SCREEN CLASS 
class GameOver(BaseState):

    def __init__(self, game):
        super().__init__(game)
        self.button = Button()
        self.screen = self.game.screen
        self.clock = self.game.clock   


     # GAME OVER SCREEN GAME STATE 
    def GameOver_Screen(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.colliderect(event.pos):
                        print("Restarted")
                    elif main_menu_button.colliderect(event.pos):
                        print("MAIN MENU")
                    elif quit_button.colliderect(event.pos):
                        pygame.quit()
                        sys.exit()

            self.screen.fill(BLACK)

            # DRAW THE GAME OVER SCREEN BACKGROUND
            gameover_bg = pygame.image.load(GAMEOVER_SCREEN_IMG)
            gameover_bg = pygame.transform.scale(gameover_bg, (WIDTH, HEIGHT))
            self.screen.blit(gameover_bg, (0, 0))

            # DRAW THE GAME OVER SCREEN TEXT
            gos_txt = self.font4.render("GAME OVER", True, WHITE)
            self.screen.blit(gos_txt, (375, 100))

            # DRAW THE BUTTONS FOR THE GAME OVER SCREEN
            restart_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Restart", WHITE, self.font1, BLACK)
            main_menu_button = self.button.draw_button(self.screen, 500, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Main Menu", WHITE, self.font1, BLACK)
            quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)
        
            # UPDATE THE GAME OVER SCREEN
            pygame.display.flip()
            self.clock.tick(FPS)