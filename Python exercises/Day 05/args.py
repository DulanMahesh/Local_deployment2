#example
def example (*args):
    total=0
    for arg in args:
        total = total+arg
    return total

print(example(1,11,15))



#example 2
def example1(*args):

    return sum(args)

print(example(1,10,670))