class Hobbit:
  def __init__(self, name = str, disposition = "homebody"):
    self.name = name
    self.disposition = disposition
    self.age = 0

  def celebrate_birthday(self):
    self.age += 1

  def is_adult(self):
    if self.age <= 32:
      return False
    else:
      return True 
    #Can be written as return self.age >= 3

  def is_old(self):
    if self.age >= 101:
      return True
    else:
      return False
    #Can be written as return self.age >= 101
    
  def has_ring(self):
    if self.name == "Frodo":
      return True
    else:
      return False

  def is_short(self):
    return True