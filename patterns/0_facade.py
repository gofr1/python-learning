class SubSystemA:

    def method1(self):
        print('SubSystemA method1')
    
    def method2(self):
        print('SubSystemA method2')

class SubSystemB:

    def method1(self):
        print('SubSystemB method1')
    
    def method2(self):
        print('SubSystemB method2')

class Facade:

    def __init__(self):
        self._SubSystem_A = SubSystemA()
        self._SubSystem_B = SubSystemB()

    def method(self):
        self._SubSystem_A.method1()
        self._SubSystem_A.method2()
        self._SubSystem_B.method1()
        self._SubSystem_B.method2()


def main():
    facade = Facade()
    facade.method()

if __name__ == '__main__':
    main()