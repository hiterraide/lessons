n = "\nПривет! Меня зовут бот, я хочу узнать о тебе все:"
n += "\nВведите “out” для завершения программы"
active = True
while active:
    message = input(n)
    if message == "out":
        active = False
    else:
        print(message)
