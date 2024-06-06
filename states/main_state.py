import pygame
import random
import math
import os 
import sys 

from scripts.settings import *
from scripts.asteroids import Asteroid
from scripts.player import Player

from scripts.buttons import Button
from states.gameover_state import GameOver


# THE MAIN GAME CLASS 
class InGame:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        self.font1 = pygame.font.Font(None, 30)
        self.font2 = pygame.font.Font(FONT2, 125)
        self.font3 = pygame.font.Font(FONT3, 125)
        self.font4 = pygame.font.Font(FONT4, 125)
        self.button = Button()

        

        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.spawn_rate = 100  # Adjust spawn rate as needed
        self.spawn_counter = 0
        # Bullet variables



       
    
    def check_collisions(self, player, asteroids):
        for asteroid in asteroids:
            if player.rect.colliderect(asteroid.rect):
                GameOver().GameOver_Screen()

    def main_game(self):
        # Main game loop
        self.paused = False 
        while True:

            # Process input/events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                    
            
                
            if not self.paused:
                # Update
                self.all_sprites.update()
                # Spawn asteroids
                self.spawn_counter += 1
                if self.spawn_counter >= self.spawn_rate:
                    asteroid = Asteroid()
                    self.all_sprites.add(asteroid)
                    self.asteroids.add(asteroid)
                    self.spawn_counter = 0
                
            
                # Draw / render
                self.screen.fill(BLACK)
                self.all_sprites.draw(self.screen)
                self.all_sprites.update()
                self.check_collisions(self.player, self.asteroids)

                # Update the display
                pygame.display.flip()
                self.clock.tick(FPS)
            
            else: 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if resume_button.collidepoint(pygame.mouse.get_pos()):
                        self.paused = False
                    elif restart_button.collidepoint(pygame.mouse.get_pos()):
                        print('Restart Screen')
                    elif options_button.collidepoint(pygame.mouse.get_pos()):
                        print('Options Screen')
                    elif quit_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

                # DRAW THE TITLE SCREEN NAME
                pause_screen_text = self.font2.render("PAUSED", True, WHITE)
                self.screen.blit(pause_screen_text, (375, 200))
                resume_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Resume", WHITE, self.font1, BLACK)
                restart_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Restart", WHITE, self.font1, BLACK)
                options_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
                quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)
                
                pygame.display.flip()
        
        
            

