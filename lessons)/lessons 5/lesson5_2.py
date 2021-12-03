money = int(input('Введите сумму:'))
procent = int(input('Введите процент:'))
for a in range(5):
        a = a+1
        money = money+money*(procent/100)
        print(int(money))
