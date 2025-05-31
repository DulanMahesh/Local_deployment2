
#Create a While Loop that subtracts one by one the numbers from 50 to 0
# (both numbers included) with the following additional conditions:
#If the number is divisible by 5, show that number on the screen
# (remember that here you can use the modulus operation dividing by 5 and checking the remainder!)
#If the number is not divisible by 5, continue executing the loop without showing the value on the screen
# (don't forget to continue subtracting so that the program doesn't run infinitely).

number = 50

while number >= 0:
    if number%5==0:
        print(number)

    number -= 1




