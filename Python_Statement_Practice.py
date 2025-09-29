# print the strings starts with 's' using split() function
str_value="Print Only the words that start with  s in the sentenst"
str_list=str_value.split(" ")
print(str_list)
for j in str_list:
    if j.startswith('s'):
        print(j)
        
# using range() function to print all even number 0 to 10

even_value=[j for j in range(0,11) if j%2==0]
print(even_value)

#use list comprehension to print 1 to 50 numbers which are % divisible by 3
divisible_three_value=[i for i in range(0,51) if i%3==0]
print(divisible_three_value)

str_value="Print every word in this sentence that has an even number of letters"
str_list=str_value.split(" ")
even_list=[val for val in str_list if len(val)%2==0]
print(even_list)

#print 1 to 50 if the number multiple by 3 print "Fizz" if the number multiple by 5 print "Buzz" otherways if the number multiple by 3 and 5 print("FizzBuzz")
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
#print first letter of every word in string below
str_value="Create a list of the first letters of every word in this string"
str_list=str_value.split(" ")
for word in str_list:
    print(word[0],end=",")
