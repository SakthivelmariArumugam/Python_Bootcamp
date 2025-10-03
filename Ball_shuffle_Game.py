import random

k=['','0','']
count=0
shuffle_list=[]
choose_value=-1
def shuffle_the_ball(k):
    random.shuffle(k)
    return k
def user_choose():
    val=-1
    while val not in [0,1,2]:
        val=int(input("User choose and one 1,2,3"))
    return val
def result(shuffle_list,choose,count):
    count=count+1
    if shuffle_list[choose]=='0':
        print(shuffle_list," ",choose)
        return "The User Win The match"
    elif count<=3:
        shuffle_list=shuffle_the_ball(shuffle_list)
        choose_value=user_choose()
        return result(shuffle_list,choose_value,count)
    else:
        return "You Don't have luck Today Try Later"

shuffle_list=shuffle_the_ball(k)
choose_value=user_choose()
print(result(shuffle_list,choose_value,0))



