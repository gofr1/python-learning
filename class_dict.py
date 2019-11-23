import random

# функция выдает рандомное число от 1 до 10 
# нужно для имитации голода и веселья
def get_random(): 
    digit = random.randint(1,5)
    return digit

def catch_ex (num):
    try:
        num = int(num)
    except ValueError:
        print("введено не число!")
        num = 0
    except Exception:
        print("ошибка")
        num = 0   
    return num


def how_much(what):
    if what == "2":
        action = int(input("Сколько скормить вашей зверушке: "))
    elif what == "3":
        action = int(input("Сколько вы хотите поиграть с вашей зверушкой: "))
    else:
        return 0
    # обрабатываем то, что ввел пользователь и обрезаем значения
    if action < 1:
        action = 1
    elif action > 30:
        action = 30
    return action

class Critter(object):
    cnt = 0
    dict = {}

    def __init__(self, name, hunger = 0, boredom = 0):
        print("Created")
        self.name = name
        self.hunger = get_random()
        self.boredom = get_random()
        self.__class__.dict.update(
            {self.__class__.cnt: {
                "Name": self.name, 
                "Hunger": self.hunger, 
                "Boredom": self.boredom 
                }
            }) # пишем имя и прочее в словарь
        self.__class__.cnt += 1 # считаем сколько объектов создано
        
    # закрытый (приватный) метод имитирующий течение времени.
    # будет вызваться из других методов
    def __pass_time(self):
        for x in self.dict:
            self.dict[x]["Hunger"] += get_random()
            self.dict[x]["Boredom"] += get_random()
    
    def __str__(self): # Показываем текущее состояние объектов
        result = "Зверей cоздано: " + str(self.cnt) + "\n"
        for x in self.dict:
            result += "\tИмя: " + self.dict[x]["Name"] + "\n"
            result += "\tГолод: " + str(self.dict[x]["Hunger"]) + "\n"
            result += "\tГрусть: " + str(self.dict[x]["Boredom"]) + "\n"
        return result

    # превратил в метод - иначе свойство невозможно выхвать с параметром
    def mood (self, critter_num):
        unhappiness = self.__class__.dict[critter_num]["Hunger"] + self.__class__.dict[critter_num]["Boredom"] 
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m 

    def talk(self, critter_num):
        print("Меня зовут", self.__class__.dict[critter_num]["Name"] , "и сейчас я чувствую себя", self.mood(critter_num), ".\n")
        self.__pass_time()

    # Кормление - уменьшает уровень голода
    def eat(self, critter_num, food = 20):
        print("Мррр... Спасибо!")
        self.dict[critter_num]["Hunger"] -= food
        if self.dict[critter_num]["Hunger"] < 0:
            self.dict[critter_num]["Hunger"] = 0
        self.__pass_time()
        #print (food)

    # Игра - уменьшает уровень скуки
    def play(self, critter_num, fun = 20):
        print("Уиии!")
        self.dict[critter_num]["Boredom"] -= fun
        if self.dict[critter_num]["Boredom"] < 0:
            self.dict[critter_num]["Boredom"] = 0
        self.__pass_time()
        #print (fun)
    
    def critter_del(self, critter_num):
        self.dict.pop(critter_num)

def crit_menu(crit, critter_num):
    # меню
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверушка
            0 - Выйти
            1 - Узнать о самочувствии зверушки
            2 - Покормить зверушку
            3 - Поиграть со зверушкой
            """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверушкой
        elif choice == "1":
            crit.talk(critter_num)
        # кормление зверушки
        elif choice == "2":
            crit.eat(critter_num, food = how_much(choice))
        # игра со зверушкой
        elif choice == "3":
            crit.play(critter_num, fun = how_much(choice))
        elif choice == "6":
            print(crit)
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

def main_menu ():
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверушка
            0 - Выйти
            1 - Создать зверушку
            2 - Узнать о состоянии зверей
            3 - Перейти в меню зверушки
            4 - Удалить зверушку
            """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # создание зверушки
        elif choice == "1":
            crit_name = input("Как вы назовете свою зверушку? ")
            crit = Critter(crit_name)
        # Узнать о состоянии зверей
        elif choice == "2":
            print(crit)
        # Перейти в меню зверушки
        elif choice == "3":
            critter_num = input("Введите номер зверушки: ")
            critter_num = catch_ex(critter_num)
            crit_menu(crit, critter_num)
        # Удалить зверушку
        elif choice == "4":
            critter_num = input("Введите номер зверушки: ")
            critter_num = catch_ex(critter_num)
            crit.critter_del(critter_num)
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main_menu()