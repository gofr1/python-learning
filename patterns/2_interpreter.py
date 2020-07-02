from abc import ABC, abstractmethod

class AbstractExpression():
    @abstractmethod
    def interpret(self):
        pass

class NonTerminalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print('Non-terminal expression being interpreted...')
        self._expression.interpret()

class TerminalExpression(AbstractExpression):

    def interpret(self):
        print('Terminal expression being interpreted...')

def main():
    ast = NonTerminalExpression(NonTerminalExpression(TerminalExpression()))
    ast.interpret()

if __name__ == '__main__':
    main()