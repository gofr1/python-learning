# Зверушка со свойствами
# Демонстрирует свойства
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустым!")
        else:
            self.__name = new_name
            print("Имя успешно изменено")
    def talk(self):
        print("\nПривет меня зовут", self.name)

# основная часть
crit = Critter("Бобик")
crit.talk()

print(crit.name)
crit.name = "Мурзик"
print(crit.name)