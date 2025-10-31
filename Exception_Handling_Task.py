try:
    for i in ['a','b','c']:
        print(i*value)
except:
    print("The TypeError Occured Here")
finally:
    print("The Programme Runned Successful")

try:
    a=10/0
except ZeroDivisionError:
    print("The zerodivisionerror occured")
finally:
    print("The Programme Runned Successful")

def number():
    while True:
        try:
            num1=int(input("Enter the number"))
        except:
            print("It's Not A Number")
            continue
        else:
            print("The Square Value Of The Number:",num1*num1)
            break
number()
        
