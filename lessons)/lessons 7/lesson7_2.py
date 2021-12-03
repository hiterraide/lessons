print("1+2+3+...+n")
n = int(input("Введите конечное значение:"))
s=0
i=1
while i<=n:
    s+=i
    i+=1
    print("Сумма", s)
print("Конечная сумма ", s)
