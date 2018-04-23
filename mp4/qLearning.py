# # This file will be used to do part 1 of the MP

class qlearn:
    
  def __init__(self):
    self.q_matrix = {}

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
