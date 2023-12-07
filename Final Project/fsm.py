class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state

    def add_transition(self, input_symbol, state, action=None, next_state=None):
        if next_state == None:
            self.state_transitions[(input_symbol, state)] = (action, state)
        else:
            self.state_transitions[(input_symbol, state)] = (action, next_state)     

    def get_transition(self, input_symbol, state):
        return self.state_transitions[(input_symbol, state)]

    def process(self, input_symbol):
        a, self.current_state = self.get_transition(input_symbol, self.current_state)

        if a != None:
            a()
