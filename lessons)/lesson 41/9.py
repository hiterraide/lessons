import math
x = int(input("Введите значение х: "))
y = int(input("Введите значение y: "))
if x == abs(x) and y == abs(y):
    print("1")
elif x != abs(x) and y == abs(y):
    print("2")
elif x != abs(x) and y != abs(y):
    print("3")
elif x == abs(x) and y != abs(y):
    print("4")
