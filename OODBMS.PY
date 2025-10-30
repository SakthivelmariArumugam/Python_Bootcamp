
class Employee:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age 
    
    def display_info(self):
        print(f"id:{self.id}\n name:{self.name} \n age:{self.age}")

class oodbms:
    def __init__(self):
        self.Objects=[]
    
    def store(self,obj):
        self.Objects.append(obj)
    
    def retrieve(self,id):
        for obj in self.Objects:
            if isinstance(obj,Employee) and obj.id==id:
                return obj.age
        return None 

e1=Employee(1,"Sakthi",21)
e2=Employee(2,"Varun",22)
e1.display_info()
e2.display_info()
o1=oodbms()
o1.store(e1)
o1.store(e2)
print("The id person age:",o1.retrieve(2))
print("The id person age:",o1.retrieve(3))
