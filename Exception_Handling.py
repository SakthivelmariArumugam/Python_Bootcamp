print("Exception Handling Example One")
def add(num1,num2):
    sum1=0
    sum1=num1+num2
try:
    num1=10
    num2=input("Enter the second number:")
    add1(num1,num2)
except:
    print("Type Error occcured")
else:
    print("the two numbers added successful")

print("Exception Handling Example Two")
    
try:
    file1=open("the new file",'r')
    file1.write("Hello Everyone")
except:
    print("The Error occured")
else:
    print("The file opened successful")
    
print("Exception Handling Example Three")
def ask_number():
    try:
        num1=int(input("Enter the number"))
    except:
        print("it's not a number")
    else:
        print("Yeah You Enter Right It's A number")

ask_number()

def add_two_values(num1,num2):
    while True:
        try:
            return num1+num2
        except:
            sum2=int(input("Enter the number:"))
            print("The sum value:",add_two_values(num1,sum2))
        else:
            print("The added Two Values Is Successful")
            break
        finally:
            print("The added Two value Successful")
            break

num1=10
num2=input("Enter the number:")
print("the sum value:",add_two_values(num1,num2))
