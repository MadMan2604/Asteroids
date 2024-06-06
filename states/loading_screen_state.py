# the script for the loading screen state
import pygame 
import sys 

from scripts.settings import *
from states.base_state import BaseState

class LoadingScreen(BaseState):
    def __init__(self, game):
        super().__init__(game)
        