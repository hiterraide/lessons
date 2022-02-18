class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.adometr = 0
    def descript_name(self):
        print(f"Марка: {self.mark}, Модель: {self.model}, Год: {self.year}")
    def read_adometr(self):
        print(f"Значение адометра: {self.adometr}")
    def update_adometr(self, n):
        if n < self.adometr:
            print(f"Пробег скинуть невозможно")
        else:
           self.adometr = n
    def increment_adometr(self, m):
            self.adometr+=m
            print(f"Новый пробег: {self.adometr}")
class Electrocar(Car):
    def __init__(self, mark, model, year, batareya):
        Car.__init__(self, mark, model, year)
        self.batareya = batareya
        print(f"Марка: {self.mark}, Модель: {self.model}, Год: {self.year}, Батарея: {self.batareya}")
    def read_batareya(self, z):
        self.batareya = z
        print(f"Значение батареи: {self.batareya}")
    def coins(self, user):
        if user < 1000000:
            print("Вам пора на небоооо за звёздоооочкоой")
        else:
            print("Машина ваша!")
        
        
        




            
my_car =  Car("Telsa", "TeslaX", 2021)
my_car.descript_name()
my_car.adometr = 23
n = int(input("update:"))
m = int(input("increment:"))
my_car.read_adometr()
my_car.update_adometr(n)
my_car.increment_adometr(m)

z = int(input("Значение батареи:"))
my_electrocar = Electrocar("Tesla", "TeslaX", 2022, z)
my_electrocar.read_batareya(z)
user = int(input("Сколько вы можете предложить?"))
my_electrocar.coins(user)



