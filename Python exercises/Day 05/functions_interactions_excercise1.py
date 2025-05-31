
#stick shuffeling Game

from random import *

#create a list of sticks

stickes =['-','--','---','----']

#shuffle the sticks

def mix(my_list):

    shuffle(my_list)
    return(my_list)

#ask player to choose number between 1 to 4

def try_your_luck():
    a_try='' # to store players selection
    while a_try not in['1','2','3','4']:
        a_try=input("Choose a number(1 to 4) : ")

    return int(a_try)

#check players try

def verify_try(a_list,a_try):
    if a_list[a_try-1] == '-':   # if the user selction is one stick
        print("wash the dishes")
    else:
        print("This time you are safe!!")
    print(f'you got {a_list[a_try-1]}')


#now we give the interactions between functions in order to play the game

mixed_sticks= mix(stickes) # shuffle the sticks
selection =try_your_luck() #ask the player for their choice
verify_try(mixed_sticks,selection) # check the result




