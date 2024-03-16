class Medusa:
  def __init__(self, name = str, statues = list):
    self.name = name
    self.statues = []

  def stare(self, victim):
    if len(self.statues) <= 2:
      self.statues.append(victim)
      victim.stoned = True
    elif len(self.statues) == 3:
      self.statues[0].stoned = False
      self.statues.pop()
      self.statues.append(victim)
      victim.stoned = True



  