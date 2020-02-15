# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Player(object):
    """ Игрок в экшен-игре """
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """ Враждебный пришелец-инопланетянин в экшен-игре """
    def die(self):
        print("Пришелец погибает")

# основная часть
print("\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
