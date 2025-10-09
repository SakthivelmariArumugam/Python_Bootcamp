
def position_choice():
    choice="wrong"
    
    while choice not in ['0','1','2']:
        choice=input("Enter the choice only in ['0','1','2']:")
        if choice not in ['0','1','2']:
            print("Sorry I Can't Understootd Select Choice From This [0,1,2")
    return int(choice)

def Replacement_choice(list_value,position):
    value=input("Enter Replacement value:")
    list_value[position]=value
    return list_value

def game_on():
    choice='wrong'
    while choice not in ['y','n']:
        choice=input("Enter the choice only 'y' or 'n':")
        if choice not in ['y','n']:
            print("Sorry the computer not understand")
    
    return choice
    
game='y'

while game=='y':
    position=position_choice()
    list_value=['0','1','2']
    result=Replacement_choice(list_value,position)
    print(result)
    game=game_on()
    
