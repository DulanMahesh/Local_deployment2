'''Create a function (sum_less) that adds the numbers of a list as long as
they are greater than 0 and less than 1000, and returns the result of said sum.
Create a numbers variable, storing a list of numbers so we can test it.'''


def sum_less(numbers):
    total=0
    for n in numbers:
        if n>0 and n<1000:
            total =total+n
        else:
            pass
    return total

print(sum_less([10,100,-1,990]))



