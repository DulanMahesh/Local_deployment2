my_list =['A','B','C']
my_list2 =['E','F','G']
NEW_LIST =my_list+my_list2 # CONCATANATION IN LISTS
print(NEW_LIST)

my_list[0]="Alpha" #assign a new value to the first element of the list
print(my_list)

my_list.append("crescat")# new item will be added next to the last existing element
print(my_list)

my_list.pop()# remove the last element form the list
print(my_list)

deleted_element =my_list.pop(1)#remove element 1 from the list and put that removed item in a variable to use later
print(deleted_element)

new_list =[1,20,23,2,67]
new_list.sort()# sort
print(new_list)
new_list.reverse()
print(new_list)# reverse