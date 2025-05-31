#exercise 1

def sum(num1,num2):
    return (num1+num2)

reult=sum(10,20)

print(reult)

#exercise2

def mulitiply(num1,num2):
    return (num1*num2)

print(mulitiply(10,20))

#exercise3

'''Create a function called reverse_word that takes the characters of a given word as an argument,
 reverses the order of their characters, and returns them that way and in uppercase.
For example, if we pass it the word "Python", it should return: "NOHTYP"
Also, you must create a variable called word, which contains any string, to pass it as an argument to the created function.'''

def reverse_word(word):
    reverse_output = (''.join(reversed(word))) # revsered object is joined with a string to show an output.without joining with a string it would be an iterator only
    uppercase_reversed = reverse_output.upper()
    print(uppercase_reversed)
    return uppercase_reversed


reverse_word('python')


