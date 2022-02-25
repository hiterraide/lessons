age = int(input("возраст?"))
work = int(input("доход?"))
if age < 18:
    print("Вам нельзя брать кредит")
elif work < 3000:
    print("Вам нельзя брат кредит")
else:
    print("Alles gut")
