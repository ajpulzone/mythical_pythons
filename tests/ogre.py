class Ogre:
  def __init__(self, name = str, home = "Swamp"):
    self.name = name
    self.home = home
    self.encounters = 0
    self.swings = 0

  def encounter(self, human):
    # human.ogre_saw += 1
    human.encounter_counter += 1
    if human.notices_ogre():
      self.swing_at(human)

  def swing_at(self, human):
    if human.notices_ogre():
      self.swings += 1
      human.swung_at += 1