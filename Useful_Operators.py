
for i in range(10):
    print(i)
    
print(list(range(0,11,2)))

name="Sakthi"
count=0 

for i in name:
    print(f"{i} and {count}")
    count=count+1
    
#Replace The Index_count Python using enumerate
name="cognizant"
for char in enumerate(name):
    print(char)

#zip function we can combine the multiple list like zip(list1,list2,list3)
list1=[1,2,3]
list2=["sakthi","Johnson","smith"]
list3=[100,99,98]
for val in zip(list1,list2,list3):
    print(val)

list1=[1,2,3]
list2=["vinay","Anderson","kavin"]
list3=[99,88,99,77]
for val in zip(list1,list2,list3):
    print(val)

#check the value in the list using in keyword

print('x' in ['x','y','z'])

print(100 in [99,88,101])

print('name' in {'name':"sakthi",'age':21})

#shuffle method get from random library and used for shuffle the list

from random import shuffle
import random
mylist=["Apple","Ball","Cat","Dog"]
print(mylist)
shuffle(mylist)
print(mylist)
mylist2=random.sample(mylist,k=len(mylist))
print(mylist2)

#random library have the randint function.it's to you can get any of the random value between the range
from random import randint
print(randint(0,100))

