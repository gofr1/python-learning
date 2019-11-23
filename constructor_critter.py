# Зверушка с конструктором
# Демо метода-конструктора
class Critter(object): # заголовок класса
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверушка!")
    def talk(self):
        print("Привет. Я зверушка - экземпляр класса Critter")
# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()