import random
matrix=[[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]

choice_list=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
Start=True


def user_choice():
    a=-1
    b=-1
    if not choice_list:
        return []
    while [a,b] not in choice_list:
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])
            
        a=int(input(f"Enter Choice {choice_list} in this list:"))
        b=int(input(f"Enter Choice {choice_list} in this list:"))
    
    choice_list.remove([a,b])
    return [a,b]

def computer_choice():
    if not choice_list:
        return[]
    value=random.choice(choice_list)
    choice_list.remove(value)
    return value
def Check_result():
    for i in range(3):
        count1=0
        count2=0
        for j in range(3):
            if matrix[i][j]=='X':
                count1=count1+1
            if matrix[i][j]=='O':
                count2=count2+1 
    for i in range(3):
        count3=0
        count4=0
        for j in range(3):
            if matrix[j][i]=='X':
                count3=count3+1
            if matrix[j][i]=='O':
                count4=count4+1 
    
    if (matrix[0][0]=='X' and matrix[1][1]=='X' and matrix[2][2]=='X') or (matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
        return True
    if (matrix[0][2]=='X' and matrix[1][1]=='X' and matrix[2][0]=='X') or (matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
        return True
    if count1==3 or count2==3 or count3==3 or count4==3:
        return True
    return False
def Game(matrix):
    Start=True
    user=True
    computer=False
    while True:
        if user==True:
            result_u=user_choice()
            if not result_u:
                return "Match Tie"
            matrix[result_u[0]][result_u[1]]='X'
            result=Check_result()
            if result:
                return "You Win The Game"
            computer=True
            user=False
        if computer==True:
            result_c=computer_choice()
            if not result_c:
                return "Match Tie"
            matrix[result_c[0]][result_c[1]]='O'
            result=Check_result()
            if result:
                return "You Lose The Game"
            computer=False
            user=True
        if len(choice_list)==0:
            return
        
print(Game(matrix))
print(matrix[0])
print(matrix[1])
print(matrix[2])
            
