class Animal:
    def __init__(self):
        print("Animal Class Created")
    def name(self):
        print("Animal Name is Lion")
    def who_am_i(self):
        print("King Of Forest")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Class Created")
    def pet_name(self):
        print("Dog name is Monish")

Dog1=Dog()
Dog1.name()
Dog1.who_am_i()
Dog1.pet_name()
