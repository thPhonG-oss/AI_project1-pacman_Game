class Entity:

    def __init__(self, xPos, yPos, size):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.dead = False

    def draw(self):
        pass

    def update(self):
        pass

    def getRect(self):
        pass

    def getSize(self):
        return self.size

    def isDead(self):
        return self.dead

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setDead(self):
        self.xPos = -32
        self.yPos = -32
        self.dead = True