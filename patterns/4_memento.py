#!/usr/bin/env python3

# memento pattern
# captures the internal state of an object
# restores the same state if needed

import pickle

class Originator:

    def __init__(self):
        self._state = None
    
    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return pickle.dumps(vars(self))

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

def main():
    orig = Originator()
    print(vars(orig))

    memento = orig.create_memento()
    orig.set_state(True)
    print(vars(orig))

    orig.set_memento(memento)
    print(vars(orig))

if __name__ == '__main__':
    main()