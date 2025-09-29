#Begineer Convert The Strint To List format

name="Sakthivelmari"
name_list=[]
for i in name:
    name_list.append(i)

print(name_list)

#String Convert To List Format Using list() function
name="Cognizant"
name_list=list(name)
print(name_list)

#we can do this without using list() function
name="Earth"
name_list=[letter for letter in name]
print(name_list)

#Number with Example
num_range=[x*2 for x in range (1,11)]
print(num_range)

#Fahrenhit With Example
temperature=[((9/5*x)+32) for x in range(31,41)]
print(temperature)

#if else statement using to create a list
num_list=[x if x%2==0 else "ODD" for x in range(1,11)]
print(num_list)

#normal nested loop multiplication
num_nested_list=[]
for i in [2,4,6]:
    for j in [1,10,1000]:
        num_nested_list.append(i*j)

print(num_nested_list)

#nestloop inside the list
num_nested_list=[x*y for x in [2,4,6] for y in [1,10,100]]
print(num_nested_list)
        
