#exercise01
def a_sum(**kwargs):
    total=0
    for key,value in kwargs.items():
        print(f'{key}={value}')
        total=total+value
    return total

print(a_sum(x=5,y=7,z=9))


#excercise02
#lets put all kind of argument and see how they behave
def test(number1,number2,*args,**kwargs):
    print(f'The first number is {number1}')
    print(f'The second number is {number2}')

    for arg in args:
        print(f'arg ={arg}')

    for key,value in kwargs.items():
        print(f'{key} = {value}')

test(10,20,30,40,50,60,x=70,y=80,z=90)

#exercise03
def test3(number1,number2,*args,**kwargs):
    print(f'The first number is {number1}')
    print(f'The second number is {number2}')

    for arg in args:
        print(f'arg ={arg}')

    for key,value in kwargs.items():
        print(f'{key} = {value}')

args =[30,40,50,60]
kwargs={'x':70,'y':80,'z':100}

test(10,20,*args,**kwargs)










