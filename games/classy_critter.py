# Классово верная зверушка
# Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0 # атрибут класса
    @staticmethod # декоратор 
    def status():
        print("\nВсего зверушек сейчас", Critter.total)
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.name = name # и создание атрибута
        Critter.total += 1 # увеличиваем значение в счетчике на один
# основная часть
print("Нахожу значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("\nСоздаю зверушек")
crit1 = Critter("Первый")
crit2 = Critter("Второй")
crit3 = Critter("Третий")

Critter.status()
print("\nОбращаюсь к атрибуту класса через объект:", end = " ")
print(Critter.total)
