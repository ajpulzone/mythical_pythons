class Centaur:
    def __init__(self, name = str, breed = str):
        self.name = name
        self.breed = breed
        self.action_counter = 0
        self.is_standing = True
        self.is_laying = False

    def shoot(self):
        if self.is_standing == False and self.is_laying == True:
            return 'NO!'
        elif self.action_counter >= 3:
            return 'NO!'
        else:
            self.action_counter += 1
            return 'Twang!!!'
    
    def run(self):
        if self.is_standing == False and self.is_laying == True:
            return 'NO!'
        self.action_counter += 1
        return 'Clop clop clop clop!'
    
    def is_cranky(self):
        return False if self.action_counter < 3 else True
    
    def sleep(self):
        if self.is_standing:
            return 'NO!'
        else:
            self.action_counter = 0
        
    def lay_down(self):
        self.is_standing = False
        self.is_laying = True

    def stand_up(self):
        self.is_standing = True
        self.is_laying = False
