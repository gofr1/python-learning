# Зверушка с атрибутами
# Демонстрирует создание атрибутов и работы с ними
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name): # инициализация объекта
        print("Появилась на свет новая зверушка!")
        self.name = name # и создание атрибута
    def __str__(self): # если распечатать объект сделает то, что написано здесь
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name +"\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")

# основная часть

crit1 = Critter("Барбос")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print("Вывод объекта crit1 на экран")
print(crit1)

print("Непосредственный доступ к crit1.name")
print(crit1.name)

