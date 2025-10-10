class Dog:
    def __init__(self,breed,name,age):
        self.breed=breed
        self.age=age
        self.name=name

dog1=Dog("Bull Dog","Monish",21)
print(dog1.breed)
print(dog1.name)
print(dog1.age)

class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    
    def circumference(self):
        print(f"The {self.radius} radius of circle circumference is {2*self.radius*self.pi}")

c1=Circle()
print(c1.pi)
print(c1.radius)
c1.circumference()
        
