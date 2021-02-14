from dataclasses import dataclass

@dataclass
class Player:
    id: int
    name: str
    keys: set 

if __name__ == '__main__':
    p1 = Player(1, 'John', {'red', 'blue'})
    print(repr(p1))

#* Player(id=1, name='John', keys={'red', 'blue'})