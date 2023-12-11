import pygame
from fsm import FSM

class Steak():
    def __init__(self, game, x = 137, y = 260):
        self.game = game
        # self.raw_img = pygame.image.load("steak.png")
        # self.cooked_img = pygame.image.load("cooked.png")
        self.states = ["Raw", "Rare", "Medium Rare", "Medium", "Medium Well", "Well Done", "Burnt"]
        self.current_state = "Raw"

        self.fsm = FSM()
        self.init_fsm()
    
    def init_fsm(self):
        self.fsm.add_transition(True, "Raw", None, "Rare")
        self.fsm.add_transition(False, "Raw", None, "Raw")
        self.fsm.add_transition(True, "Rare", None, "Medium Rare")
        self.fsm.add_transition(False, "Rare", None, "Rare")
        
    # def change_state(self):
