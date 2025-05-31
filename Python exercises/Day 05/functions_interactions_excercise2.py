'''Create a function (throw_dice) that "throws" two random dice and returns its results
 (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).

Pass the result of these two dice to a function called roll_result
 (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message
  according to the what the sum of these values results:

If the sum is less than or equal to 6:

"The sum of your dice is {sum_dice}. Unfortunate"

If the sum is greater than 6 and less than 10:

"The sum of your dice is {sum_dice}. You have a good chance"

If the sum is greater than or equal to 10:

"The sum of your dice is {sum_dice}. It looks like a winning roll"'''

import random

#create two random selections for two dices

#Throw 2 dices
def throw_dice():
    dice_01 = [1, 2, 3, 4, 5, 6]
    dice_02 = [1, 2, 3, 4, 5, 6]
    random_dice_01 =random.choice(dice_01)
    random_dice_02=random.choice(dice_02)

    return random_dice_01, random_dice_02

#print(throw_dice(dice_01,dice_02))


def roll_result(random_dice_01,random_dice_02):
    sum_dice= random_dice_01 + random_dice_02
    if (random_dice_01+random_dice_02) <= 6:
        return (f'The sum of your dice is {sum_dice}. Unfortunate')
    elif (sum_dice) >6 and (sum_dice)<10:
        return(f'The sum of your dice is {sum_dice}. You have a good chance')
    else :
        return(f'The sum of your dice is {sum_dice}. It looks like a winning roll')

result1,result2=throw_dice()
message=roll_result(result1,result2)
print(message)