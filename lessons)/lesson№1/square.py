#Площадь треугольника по формуле Герона
import math
a = int(input("Введите 3 целых числа"))
b = int(input("Введите 3 целых числа"))
c = int(input("Введите 3 целых числа"))
p = (a+b+c) / 2
result = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Площадь треугольника", result)

