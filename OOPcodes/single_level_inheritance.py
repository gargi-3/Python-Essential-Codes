class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return f"{ self.name } says Woof-Woof!"
    
dog = Dog("Oscar")
print(dog.sound())

class Cat(Animal):
    def sound(self):
        return f"{ self.name } says Meow!"
    
cat = Cat("Lizzy")
print(cat.sound())