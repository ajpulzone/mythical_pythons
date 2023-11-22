class Unicorn:
    def __init__(self, name=str, color='silver'):
        self.name=name
        self.color=color

    def is_silver(self):
        return True if self.color == 'silver' else False

    def say(self, say):
        return f"**;* {say} **;*"