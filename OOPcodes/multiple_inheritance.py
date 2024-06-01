class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        pass

class Pet:
    def __init__(self,pet_owner):
        self.pet_owner = pet_owner
    
    def pet_food(self):
        return f"{ self.pet_owner } feeds Pet Food"
    
class Dog(Animal,Pet):
    def __init__(self,name,pet_owner,breed):
        Animal.__init__(self,name)
        Pet.__init__(self,pet_owner)
        self.breed = breed

    def sound(self):
        return f"{ self.name } sounds wooh-wooh!"
    
my_pet = Dog("Lucy","Gargi","Labrador")
print(my_pet.sound())
print(my_pet.pet_food())