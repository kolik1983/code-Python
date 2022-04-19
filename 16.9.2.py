class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        self.y

    def areaRect(self):
        return self.x * self.y


r = Rectangle(10, 2)
print('Площадь-', r.areaRect(), 'длинна и ширина - ', r.getX(), r.getY())