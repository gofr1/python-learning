# Закрытая зверушка
# Демонстрирует закрытые переменные и методы
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверушка")
        self.name = name # открытый атрибут
        self.__mood = mood # закрытый атрибут
    
    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood)
    
    def __private_method(self):
        print("Это закрытый метод.")
    
    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()

# Основная часть
crit = Critter(name = "Шарик", mood = "Отлично")
crit.talk()
crit.public_method()

# Не рекомендуется это использовать
print(crit._Critter__mood) # Вызов приватного атрибута
crit._Critter__private_method() # Вызов приватного метода
