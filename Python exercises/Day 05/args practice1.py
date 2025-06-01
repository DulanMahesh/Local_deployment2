
'''Create a function called sum_squares that takes any number
 of numeric arguments, and returns the sum of their values squared.
For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9'''

def sum_squares(*args):
    squared = []
    for a in args:
        a = a * a
        squared.append(a)

    return sum(squared)

print(sum_squares(1,3,5,7,9))
