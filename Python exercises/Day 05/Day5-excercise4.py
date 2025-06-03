'''Write a function called count_primes() that requires a single numeric argument.
This function must display on the screen how many prime numbers
there are in the range from zero to that number included, and then return the number of prime numbers found.
Note: By convention 0 and 1 are not considered primes
'''

def count_primes(num):
    counter =0
    for n in range(2,num):
        if num>1 and num%num==0:


