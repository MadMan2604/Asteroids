import pygame
import sys 

from states.state_manager import StateManager
from states.main_state import InGame
from states.titlescreen_state import TitleScreen
from states.optionsscreen_state import OptionsScreen
#from states.informationscreen_state import InformationScreen 
from states.loading_screen_state import LoadingScreen
from scripts.settings import * 

# Game class
class Game:
    def __init__(self, screen):
        self.screen = screen  
        self.clock = pygame.time.Clock()
        self.running = True 
        self.state_manager = StateManager(self)

        # Initialise and add game states
        self.state_manager.add_state("title_screen", TitleScreen(self))
        self.state_manager.add_state("loading_screen", LoadingScreen(self))
        self.state_manager.add_state("game", InGame(self))
        self.state_manager.add_state("options_screen", OptionsScreen(self))
        #self.state_manager.add_state("information_screen", InformationScreen(self))
        self.state_manager.change_state("title_screen")

        # Initialise + Define fonts
        self.font = pygame.font.Font(FONT, 80)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)
    
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False 
            
            self.state_manager.update(events)
      
            self.state_manager.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit() 