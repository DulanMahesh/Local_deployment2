#Practice  # 2
'''Indefinite Arguments (**kwargs)
Create a function called list_attributes that returns
in the form of a list the values of the attributes given
in the form of keywords. The function must expect to receive any number of arguments of this type.'''


def list_attributes(**kwargs):
    list1 = []
    for values in kwargs.values():
        list1.append(values)

    return list1
