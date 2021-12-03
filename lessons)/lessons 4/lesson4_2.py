number1 = float(input("1:"))
number2 = float(input("2:"))
if number1 > number2:
    number1 = 1
    number2 = 0
    print(number1, number2)
elif number2 > number1:
    number1 = 0
    number2 = 1
    print(number1, number2)
else:
    print("Равны")
