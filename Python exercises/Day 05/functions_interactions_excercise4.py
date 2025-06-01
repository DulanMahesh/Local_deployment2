
'''You must create a list with values and call it secret_codes.
Create a function called toss_coin that returns the result of a
 random coin toss. Such a function must be able to return the results
 "Heads" or "Tails", and must not receive any arguments to work.

Create a second function called luck, that takes two arguments:
the first must be the result of the coin toss. The second argument will be any list
(the secret_codes variable that was created at the beginning).

If the coin comes up "You must create a list with values and call it secret_codes.

Create a function called toss_coin that returns the result of a random coin toss.
 Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.

Create a second function called luck, that takes two arguments:
the first must be the result of the coin toss. The second argument will be any list
 (the secret_codes variable that was created at the beginning).

If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct",
and return said list as empty list = [ ].

If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.
Hint: Use the random library's choice method to choose an element at random from a sequence.Tails",
luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].
If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.
Hint: Use the random library's choice method to choose an element at random from a sequence.'''

import random

secret_codes = [15, 345, 456, 45, 344]


def toss_coin():
    toss_option = ['Heads', 'Tails']
    toss = random.choice(toss_option)
    return toss


def luck(toss, secret_codes):
    if toss == "Tails":
        print('List will self-destruct')
        secret_codes = []
        return secret_codes
    else:
        print('List was saved')
        return secret_codes






