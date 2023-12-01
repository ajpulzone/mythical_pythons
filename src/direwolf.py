class Direwolf:
    def __init__(self, name = str, home = 'Beyond the Wall', size = 'Massive', starks_to_protect = []):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = starks_to_protect
    
    def protects(self, stark):
        if not self.home == stark.location:
            pass
        else:
            self.starks_to_protect.append(stark)

class Stark:
    def __init__(self, name = str, location = 'Winterfell'):
        self.name = name
        self.location = location