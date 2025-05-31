

'''   : the program will ask for the user's name and then it will say
something like: “Well John, I've thought of a number between 1 and 100 and you
have only eight tries to guess it. What number do you think it is?” On each try, the
player will say a number and the program can answer for different things.
 If the number the user said is less than 1 or greater than 100, it will tell them that
he/she has chosen a number that is out of play.
 If the number the user chose is less than the number the program thought of, it will tell
them that the answer is wrong, and that he/she chose a lower number than the secret
number.
 If the user chose a number greater than the secret number, it will let them know that it
was greater.
 And if the user got the secret number right, they will be informed that they have won,
and how many tries that has taken them.
 If the user has not guessed correctly in their first attempt, they will be asked again to
choose another number and so on until they win or until their eight attempts are done. '''

from random import *

no_of_chances=8
secret_number =randint(0,100)

user_input = input("Enter your name :")
print(f"Well {user_input}! I have thought of a number between 0 and 100\n can you guess it within 8 times")
while no_of_chances>0:
    user_guess = int(input())
    no_of_chances = no_of_chances - 1
    if user_guess<secret_number:
        print("Sorry the secret number is higher than that!! ")

    elif user_guess>secret_number:
        print ("Sorry the secret number is lower than that!! ")

    else:
        print(f"you won.You guess it in {(8-no_of_chances)} times ")
        break
if secret_number != user_guess:
    print(f"we are runing out of attempts! secret no was {secret_number}")








