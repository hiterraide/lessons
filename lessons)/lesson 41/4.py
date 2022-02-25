x = int(input("Введите полученую оценку"))
if x >= 10 and x <= 12:
    print("Nice!")
elif x >= 7 and x < 10:
    print("Good")
elif x >= 4 and x < 7:
    print("Bad")
elif x < 4:
    print("Soooooooooo bad")
else:
    print("Такой оценки нет")
