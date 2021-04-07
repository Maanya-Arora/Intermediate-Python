class Species:
    def __init__(self, typee):
        self.typee = typee

    def announce(self):
        print(f"hello, i am a {self.type}")

class Human(Species):
    humancount = 0

    def __init__(self, typee, gender):
        super().__init__(typee)
        self.gender = gender
        Human.humancount += 1
    
    def displayCount(self):
        print(f"total humans: {Human.humancount}")

    def displayHuman(self):
        print(f"gender: {self.gender}")

class Person(Human):

    def __init__(self, typee, gender, name):
        super().__init__(typee)
        super().__init__(gender)
        self.name = name
    
    def displayPerson(self):
        print(f"type: {self.typee}, gender: {self.gender}, name: {self.name}")

class Animal(Species):
    animalcount = 0

    def __init__(self, typee, spec):
        super().__init__(typee)
        self.spec = spec
        Animal.animalcount += 1
    
    def displayCount(self):
        print(f"total animals: {Animal.animalcount}")

    def displayAnimal(self):
        print(f"specific type: {self.spec}")
    
    def displayFull2(self):
        print(f"type: {self.typee}, specific type: {self.spec}")

genderinput = input("you are a human. what is your gender:")
nameinput = input("your name:")
firstobject = Person('human', genderinput, nameinput)
firstobject.announce()
firstobject.displayHuman()
firstobject.displayPerson()

secondobject = Animal('animal','tiger')
thirdobject = Animal('animal','zebra')
secondobject.announce()
thirdobject.announce()
print(Animal.animalcount)
