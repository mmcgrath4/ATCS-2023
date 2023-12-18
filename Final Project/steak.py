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
            # Change to next side
            self.fsm.add_transition(2, self.states[i], None, "Raw")
        self.fsm.add_transition(2, "Burnt", None, "Raw")
        self.fsm.add_transition(True, "Burnt", None, "Burnt")
        self.fsm.add_transition(False, "Burnt", None, "Burnt")
        
        
    def get_current_state(self):
        return self.fsm.current_state

    def draw_steak(self, screen, rDiff, isUser):
        if isUser:
            pygame.draw.rect(screen, (255 - rDiff, 0, 0), (self.x, self.y, 100, 100))
        else:
            pygame.draw.rect(screen, (255 - rDiff, 0, 0), (self.x+450, self.y, 100, 100))

    def update(self, timerUp, side):
        if side > 1:
            self.fsm.process(side)
        else:
            self.fsm.process(timerUp)

