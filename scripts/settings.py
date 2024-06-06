# ALL THE GAME SETUP ITEMS ARE LOCATED HERE
import pygame 
# GAME WINDOW SETTINGS
WIDTH = 1400
HEIGHT = 800 
FPS = 60 
TITLE = "Asteroid Shooter"
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# GAME VARIABLES + FOLDER PATHS
FONT = 'assets/fonts/arial.ttf'
FONT2 = 'assets/fonts/ARCADE.ttf'
FONT3 = 'assets/fonts/Jersey-Slim.ttf'
FONT4 = 'assets/fonts/Slim-Thirteen-Pixel-Fonts.ttf'
IMG_DIR = 'assets/images/'
SOUND_DIR = 'assets/sounds'
SPRITES = 'assets/sprites/'

# GAME CONSTANTS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# TITLE SCREEN SETTINGS
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# GAME IMAGE PATHS
TITLE_SCREEN_IMG = IMG_DIR + 'title_screen_bg.png'
GAMEOVER_SCREEN_IMG = IMG_DIR + 'gameover_screen_bg.png'

# PLAYER SETTINGS
PLAYER_SPEED = 2

# BULLET SETTINGS
SHOOT_COOLDOWN = 20
BULLET_SCALE = 1.4
BULLET_SPEED = 10 
