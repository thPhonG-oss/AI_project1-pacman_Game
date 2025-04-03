class key:
    def __init__(self):
        self.isPressed = False

    def toggle(self, pressed):
        if not (pressed == self.isPressed):
            self.isPressed = pressed
    
    def getPressed(self):
        return self.isPressed
    
