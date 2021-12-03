import math
a = float(input('введите сторону треугольника'))
radius = float(input('введите радиус'))
if radius == a * math.sqrt(3)/6:
    print('можно')
else:
    print('нельзя')
