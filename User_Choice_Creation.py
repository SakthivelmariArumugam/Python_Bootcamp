choice="Wrong"
choose_range=False
acceptable_range=range(0,10)
while choice.isdigit()==False or choose_range==False:
    choice=input("Enter choice only range 0-10")
    if choice.isdigit()==False:
        print("Sorry That Wrong Choice Enter Again")
    else:
        if int(choice) in acceptable_range:
            choose_range=True

print("The User Choose Value:",choice)



