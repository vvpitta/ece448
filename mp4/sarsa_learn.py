'''
Sarsa class with functions to maintain s_matrix and seen_matrix
'''

class slearn:
    def __init__(self):
        self.s_matrix = {}
        self.state_seen = {}

    def get_s(self, state, action):
        return self.s_matrix[state][action]

    def set_s(self, state, action, value):
        self.s_matrix[state][action] = value

    def get_actions(self, state):
        return self.s_matrix[state]

    def get_smat(self):
        return self.s_matrix

    def set_smat(self, matr):
        self.s_matrix = matr

    def add_to_state(self, state):
        self.state_seen[state] += 1

    def seen_val(self, state):
        return self.state_seen[state]

    def set_seenMat(self, matr):
        self.state_seen = matr
