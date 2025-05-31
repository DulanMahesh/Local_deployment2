
'''Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list,
but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value.
The order of the elements can be changed.

For example, if given the list [1,2,15,7,2] it should return [1,2,7].

Create a function called average() that can receive as an argument
 the list returned by the previous function, and that calculates
  the average of its values. It should return the result (a float), without printing it.'''

numbers=[1,2,15,7,2]

def reduce_list(numbers):
    store=[]
    for n in numbers:
        if n not in store:
            store.append(n)
        else:
            pass
    store.remove(max(store)) # removes the maximum value from the list using max()
    return store

#print(reduce_list(numberlist))

def average (number):
    total_in_list = sum(number)
    average_of_list =float(total_in_list/len(number))
    return average_of_list


list1=reduce_list(numbers)
average_of_list=average(list1)
print(average_of_list)





