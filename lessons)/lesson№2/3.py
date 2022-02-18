cars = ["lada", "ferrari", "suzuki", "bmw"]
print("Весь список машин", cars)
user = f"Покажите мне весь список без {cars[0].title()}"
item1 = "lada"
del_item = cars.remove("lada")
print(item1)
print(user)
print("Вот держите. Список без Lada", cars)
item = f"Может вы хотите рассмотреть {cars[1].title()}"
print(item)
print(cars[1])
