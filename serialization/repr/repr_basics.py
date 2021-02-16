class Player:
    def __init__(self, id, name, keys) -> None:
        self.id = id
        self.name = name
        self.keys = keys
    
    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f'{cls}({self.id!r}, {self.name!r}, {self.keys!r})'

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO, filename='game.log')

    p1 = Player(1, 'John', {'red', 'blue'})
    logging.info('p1 is %r', p1)

# in terminal
# python3 repr_basics.py
# cat game.log 
#* INFO:root:p1 is Player(1, 'John', {'red', 'blue'})

# ipython
# In [1]: from repr_basics import Player                                                                        
# 
# In [2]: p1 = Player(1, 'John', {'red', 'blue'})                                                               
# 
# In [3]: p1.id                                                                                                 
#* Out[3]: 1
# 
# In [4]: p1.name                                                                                               
#* Out[4]: 'John'

