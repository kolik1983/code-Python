from Rectagle import Rectagle, Square, Circle

rect_1 = Rectagle(3, 4)
rect_2 = Rectagle(12, 5)
sq_1 = Square(5)
sq_2 = Square(10)
cir_1 = Circle(5)
cir_2 = Circle(22)


print(rect_1.get_Area())
print(rect_2.get_Area())

print(sq_1.get_area_sq())
print(sq_2.get_area_sq())

figures = [rect_1, rect_2, sq_1, sq_2, cir_1, cir_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_sq())
    elif isinstance(figure, Circle):
        print('Radius = ', figure.get_area_circle())
    else:
        print(figure.get_Area())