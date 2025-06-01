'''Create a function called describe_person, which takes
his name as parameters and then an indeterminate number of arguments.
 This function should display on the screen:

Characteristics of {name}:
{argument_name}: {argument_value}
{argument_name}: {argument_value}
etc...'''


def describe_person(name,**kwargs):
    print(f"Characteristics of {name}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")