class Dragon:
  def __init__(self, name = str, color = str, rider = str):
    self.name = name
    self.rider = rider
    self.color = color
    self.food_counter = 0
    
    

  def is_hungry(self):
    if self.food_counter <= 2:
      return True
    else: 
      return False
    
  def eat(self):
    self.food_counter +=1
    
