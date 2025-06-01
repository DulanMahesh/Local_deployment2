#Practice #1
'''Create a function called number_attributes that counts the number
 of parameters that are passed, and returns that number as the result.'''

def number_attributes(**kwargs):
    return len(kwargs)

print(number_attributes(x=5,y=7,z='three'))
