class Person:
    def __init__(self): # default constructor
        self.name = "Gargi Rout"
        self.age = 22

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def show(self):
        print("Person information [Name:",self.name,"Age:",self.age,"]")

    def display(self):
        print("Person information [Name:",self.name,"Age:",self.age,",Email:",self.email,"]")

# person1 = Person()
# person1.show()

person2 = Person("Shrikant",23,"shree@gmail.com")
person2.display()