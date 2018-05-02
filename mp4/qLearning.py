'''
QLearning class with functions to maintain q_matrix and seen_matrix
'''
class qlearn:

  def __init__(self):
    self.q_matrix = {}
    self.state_seen = {}

  def get_q(self, state, action):
      return self.q_matrix[state][action]

  def set_q(self, state, action, value):
    self.q_matrix[state][action] = value

  def get_actions(self, state):
    return self.q_matrix[state]

  def get_qmat(self):
      return self.q_matrix

  def set_qmat(self, matr):
      self.q_matrix = matr

  def add_to_state(self, state):
      self.state_seen[state] += 1

  def seen_val(self, state):
      return self.state_seen[state]

  def set_seenMat(self, matr):
      self.state_seen = matr
