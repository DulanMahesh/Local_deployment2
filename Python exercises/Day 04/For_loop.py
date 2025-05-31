#my_list =['a','b','c','d']

#for x in my_list:

    #print("letter:"+ x)

#for x in my_list:
    #letter_number =my_list.index(x)+1

    #print(f"letter{letter_number}:{x}")

# example2 -Loops with flow control

#my_name_list = ['dulan','eranga','suranga','dilini','ramesh']

#for name in my_name_list:
    #if name.startswith('d'):
        #print(name)
    #else:
        #print("This name does not begin with 'd'.")

# example 3

#numbers =[1,2,3,4,5]
#my_value=0

#for number in numbers:
    #my_value=number+my_value
#print(my_value)

#example 4

#numbers =[1,2,3,4,5]
#my_value=0

#for number in numbers:
    #my_value=number+my_value
    #print(my_value)


#example5

#for object in [[1,2],[3,4],[5,6],[7,8]]:
    #print(object)

#example 6

#for a,b,c in [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]:
    #print(a)
    #print(b)
    #print(c)

#example 7 - dictionary operations with for loop

#dic={'key1':'1','key2':'2','key3':'3','key4':'4',}

#for item in dic:
    #print(item)


#example 8 - dictionary operations with for loop

#dic={'key1':'1','key2':'2','key3':'3','key4':'4',}

#for item in dic.items():
   # print(item)

#example 9 - dictionary operations with for loop

#dic={'key1':'1','key2':'2','key3':'3','key4':'4',}

#for item in dic.values():
   #print(item)

##example 10  - dictionary operations with for loop

#dic={'key1':'a','key2':'b','key3':'c','key4':'d',}

#for a,b in dic.items():
   #print(a,b)

##example 11  - dictionary operations with for loop

#dic={'key1':'a','key2':'b','key3':'c','key4':'d',}

#for a,b in dic.items():
  # print(a)
  # print(b)

#exercise

list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

sum_even = 0

sum_odd = 0

for number in list_numbers:

    if number % 2 == 0:
        sum_even = sum_even + number

    else:
        sum_odd = sum_odd + number

print(f"Total of the even numbers are  {sum_even}")
print(f"Total of the odd numbers are {sum_odd}")


















