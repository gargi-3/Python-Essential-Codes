class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return f"{ self.name } says wooh-wooh!"

class Labrador(Dog):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def sound(self):
        return f"{ self.name } labrador has the color { self.color } says wooh-wooh!"
    
my_pet = Labrador("Lucy","golden-brown")
print(my_pet.sound())

my_pet1 = Dog("Lucy")
print(my_pet1.sound())
