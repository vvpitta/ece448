# # This file will be used to do part 1 of the MP

class qlearn:

  def __init__(self):
    self.q_matrix = {}
    self.state_seen = {}

  def get_q(self, state, action):
    if state in self.q_matrix.keys():
      return self.q_matrix[state][action]

  def set_q(self, state, action, value):
    if state not in self.q_matrix.keys():
        self.q_matrix[state] = [0, 0, 0]
    self.q_matrix[state][action] = value

  def get_actions(self, state):
    if state not in self.q_matrix.keys():
      self.q_matrix[state] = [0, 0, 0]
    return self.q_matrix[state]

  def get_qmat(self):
      return self.q_matrix

  def set_qmat(self, matr):
      self.q_matrix = matr

  def add_to_state(self, state):
      if state not in self.state_seen.keys():
          self.state_seen[state] = 0
      self.state_seen[state] += 1

  def seen_val(self, state):
      return self.state_seen[state]
