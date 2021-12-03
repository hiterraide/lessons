lessons = ['history','math','geography','it','pe']
number = float(input('Введите номер урока:'))
if number == 1:
    print(lessons[0])
elif number == 2:
    print(lessons[1])
elif number == 3:
    print(lessons[2])
elif number == 4:
    print(lessons[3])
elif number == 5:
    print(lessons[4])
else:
    print('Уроков нет.')
