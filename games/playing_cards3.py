# Карты 3.0
# Демонстрирует наследование в части переопределения методов

class Card(object):
    """ Одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """ Карта, номинал и масть которой не могут быть выведены на экран. """
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх. """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit) # вызываем объект базового класса (надкласса)
        # можно использовать без параметров
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up


# основная часть
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Печатаю объект", card1.__class__.__name__) # ввыодим название класса, соответствующего объекта
print(card1)
print("Печатаю объект", card2.__class__.__name__)
print(card2)
print("Печатаю объект", card3.__class__.__name__)
print(card3)
print("Переворачиваю объект", card3.__class__.__name__)
card3.flip()
print(card3)
