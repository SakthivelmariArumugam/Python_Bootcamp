import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose? Type O for Rock,1 for Paper or 2 for Scissors")
user_choice=int(input())
values=[0,1,2]
computerchoice=random.randint(0,2)
if computerchoice==0 and user_choice==1:
    print("user choice")
    print(paper)
    print("computer choice")
    print(rock)
    print("User Win")
elif computerchoice==0 and user_choice==2:
    print("user choice")
    print(scissors)
    print("computer choice")
    print(rock)
    print("Computer Win")

elif computerchoice== 0 and user_choice==0:
    print("user choice")
    print(rock)
    print("computer choice")
    print(rock)
    print("Match Tie")
elif computerchoice==1 and user_choice==0:
    print("user choice")
    print(rock)
    print("computer choice")
    print(paper)
    print("computer Win")
elif computerchoice==1 and user_choice==1:
    print("user choice")
    print(paper)
    print("computer choice")
    print(paper)
    print("Match Tie")

elif computerchoice==1 and user_choice==2:
    print("user choice")
    print(scissors)
    print("computer choice")
    print(paper)
    print("User Win")
elif computerchoice==2 and user_choice==0:
    print("user choice")
    print(rock)
    print("computer choice")
    print(scissors)
    print("User Win")
elif computerchoice==2 and user_choice==1:
    print("user choice")
    print(paper)
    print("computer choice")
    print(scissors)
    print("Computer Win")
else:
    print("user choice")
    print(scissors)
    print("computer choice")
    print(scissors)
    print("Match Tie")



