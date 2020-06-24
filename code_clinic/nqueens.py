#!/usr/bin/env python3

class NQueens:
    def __init__(self, n:int):
        self.n = n
        self.field = {}
        
        for i in range(self.n):
            self.field[i] = [0] * self.n
    
    def show(self):
        for i in range(self.n):
            print(self.field[i])
        print()
        
    def add(self, x:int, y:int):
        if x > self.n or y > self.n:
            print('You cannot put Queen here')
        else:
            self.field[x][y] = 1

    def remove(self, x:int, y:int):
        if x > self.n or y > self.n:
            print('You cannot remove Queen from here')
        else:
            self.field[x][y] = 0

    def check(self):
        # check rows
        for i in range(self.n):
            if sum(self.field[i]) > 1:
                print('Not ok!')

        # check columns
        s = 0
        for i in range(self.n):
            for c in range(self.n):
                s += self.field[c][i]
            if s > 1:
                print('Not ok!')
            s = 0
        
        # check diagonals 1
        deltas = (self.n-1) * [0]
        rows = self.field.copy()

        for i in range(self.n):
            rows[i] = deltas[:self.n-i-1] + rows[i] + deltas[:i]
        
        s = 0
        for i in range(len(rows[i])):
            for c in range(self.n):
                s += rows[c][i]
            if s > 1:
                print('Not ok!')
            s = 0

        # check diagonals 2
        rows = self.field.copy()

        for i in range(self.n):
            rows[i] = deltas[:i] + rows[i] + deltas[:self.n-i-1] 
        
        s = 0
        for i in range(len(rows[i])):
            for c in range(self.n):
                s += rows[c][i]
            if s > 1:
                print('Not ok!')
            s = 0

def main():
    d = NQueens(8)
    d.add(3,0)
    d.add(5,1)
    d.add(7,2)
    d.add(1,3)
    d.add(6,4)
    d.add(0,5)
    d.add(2,6)
    d.add(4,7)
    d.show()
    d.check()

if __name__ == '__main__':
    main()
