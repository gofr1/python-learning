class Duck: # definition of the class
    # variables inside class are usually called properties
    sound = 'Quaaack!'
    walking = 'Walk like a duck!'

    def quack(self): # methods (functions inside the class)
        print(self.sound)
    
    def walk(self):         # self - is a reference to the object 
        print(self.walking) # it used when rhe class is used to create an object

def main():
    donald = Duck() # donald is now an object of the class Duck
    donald.quack() # dot . here is a de-reference operator
    donald.walk()  # to referencemembers of the object donald
    # and we are calling methods quack and walk

if __name__ == '__main__':
    main()