class Lovisa:
  def __init__(self, title = str, characteristics = 'brilliant' ):
    self.title = title 
    self.characteristics = characteristics

  def is_brilliant(self):
    if "brilliant" in self.characteristics:
      return True
    else:
      return False
  
  def is_kind(self):
    if 'kind' in self.characteristics:
      return True
    else:
      return False
    
  def say(self, phrase=str):
    return (f'**;* {phrase} **;*')


