'''Write a function that requires an indefinite number of arguments. What this function must do is return
True if at anytime the number zero has been entered twice consecutively.
For example:
(5,6,1,0,0,9,3,5) >>>
True
(6,0,5,1,0,3,0,1) >>>
False
'''

def my_function(*args):
    for i in range(len(args) - 1):  # example for i in range(8-1)------->>for i in range(7)----->>it means i in range(0) to i in range(7)
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False


print(my_function(5,6,1,0,0,9,3,5))