class Medusa:
  def __init__(self, name = str, statues = list):
    self.name = name
    self.statues = []

  def stare(self, victim):
    self.statues.append(victim)