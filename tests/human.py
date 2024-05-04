class Human:
  def __init__(self, name = "Jane"):
    self.name = name
    self.encounter_counter = 0
    self.ogre_saw = 0

  def notices_ogre(self):
    if self.encounter_counter and self.encounter_counter % 3 == 0:
      return True
    else:
      return False

  # def is_knocked_out(self, ogre):
  #   if ogre.swings == 2 and self.ogre
  #    % 6:
  #     return True
  #   else:
  #     return False