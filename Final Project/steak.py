import pygame
from fsm import FSM

class Steak():
    def __init__(self, game, x = 137, y = 260):
        self.game = game
        self.states = ["Raw", "Rare", "Medium Rare", "Medium", "Medium Well", "Well Done", "Burnt"]
        self.current_state = "Raw"

        self.x = x
        self.y = y
        self.fsm = FSM("Raw")
        self.init_fsm()
    
    def init_fsm(self):
        for i in range(len(self.states)-1):
            self.fsm.add_transition(True, self.states[i], None, self.states[i+1])
            self.fsm.add_transition(False, self.states[i], None, self.states[i])

    def draw_steaks(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 100, 100))
        pygame.draw.rect(screen, (255, 0, 0), (self.x+1, self.y, 100, 100))
