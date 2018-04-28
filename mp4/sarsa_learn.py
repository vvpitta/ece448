'''
Sarsa Training class
'''

class slearn:
    def __init__(self):
        self.s_matrix = {}
        self.state_seen = {}

    def get_s(self, state, action):
        if state in self.s_matrix.keys():
            return self.s_matrix[state][action]

    def set_s(self, state, action, value):
        if state not in self.s_matrix.keys():
            self.s_matrix[state] = [0,0,0]
        self.s_matrix[state][action] = value

    def get_actions(self, state):
        if state not in self.s_matrix.keys():
            self.s_matrix[state] = [0, 0, 0]
        return self.s_matrix[state]

    def get_smat(self):
        return self.s_matrix

    def set_smat(self, matr):
        self.s_matrix = matr

    def add_to_state(self, state):
        if state not in self.state_seen.keys():
            self.state_seen[state] = 0
        self.state_seen[state] += 1

    def seen_val(self, state):
        return self.state_seen[state]
