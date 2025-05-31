for num in range(1,100,2):
    print(num)


my_list =list(range(1,101))
print(my_list)


##exercise-01
#Use the range() function
#and a loop to add the squares of all the numbers
#from 1 to 15 (inclusive).
#Store the result in a variable called sum_squares.

sum_squares = 0

for n in range(1,16):
    square =n*n
    sum_squares=sum_squares+square
print(sum_squares)


##exercise-02