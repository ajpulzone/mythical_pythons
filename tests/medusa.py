class Medusa:
  def __init__(self, name = str, statues = list):
    self.name = name
    self.statues = []

  def stare(self, victim):
    if len(self.statues) <= 2:
      self.statues.append(victim)
      victim.stoned = True

  