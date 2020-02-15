# Телевизор
# Имитирует телевизор
# умеет переключать каналы, и регулировать громкость
# уровень громкости и число каналов оставалось в допустимых приделах

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

class Television(object):
    """Виртуальный телевизор"""
    # инициализация аттрибутов
    def __init__(self, max_channel = 100, max_volume = 10, volume_num = 5, channel_num = 1): 
        self.max_channel = max_channel
        self.max_volume = max_volume
        self.volume_num = volume_num
        self.channel_num = channel_num

    def switch_channel(self):
        channel = 0
        while channel < 1 or channel > self.max_channel:
            channel = input("Введите номер канала: ")
            channel = catch_ex(channel)
        else:
            self.channel_num = channel
            print("Включен канал: ", self.channel_num)

    def switch_volume(self, switch):
        cur_volume = self.volume_num
        if switch == "+":
            self.volume_num += 1
        elif switch == "-":
            self.volume_num -= 1
        if self.volume_num < 1 or self.volume_num > self.max_volume:
            self.volume_num = cur_volume
        print("Уровень звука: ", self.volume_num)
    
    def current_prop(self):
        print("Канал:", self.channel_num, "Уровень звука:", self.volume_num)

def main():
    tv = Television()

    # меню
    choice = None
    while choice != "0":
        print \
            ("""
            Телевизор:
            0 - Выйти
            1 - Переключить канал
            2 - Увеличить громкость
            3 - Уменьшить громкость
            4 - Текущие данные
            """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # Переключить канал
        elif choice == "1":
            tv.switch_channel()
        # Увеличить громкость
        elif choice == "2":
            tv.switch_volume("+")
        # Уменьшить громкость
        elif choice == "3":
            tv.switch_volume("-")
        # Текущие настройки
        elif choice == "4":
            tv.current_prop()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main()