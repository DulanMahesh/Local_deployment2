'''Create a function (count_even) that counts the number of even numbers that
 exist in a list (numbers), and returns the result of said count'''

def count_even(numbers):
    count =0
    for n in numbers:
        if n%2==0:
            count =count+1
        else:
            pass
    return count

print(count_even([2,4,6,3]))