class Figures:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getWidth(self):
        return self.width
    def getHeigth(self):
        return self.heigth

rectangle = Figures(2, 4, 30, 60)
square = Figures(4, 3, 10, 10)

print(['Rectangle', rectangle.getX(), rectangle.getY(), rectangle.getWidth(), rectangle.getHeigth()])
print(['Square', square.getX(), square.getY(), square.getWidth(), square.getHeigth()])