#list1 =['a','b','c']
#index =0

#for l in list1:
    #print(index,l)
    #index =index+1


#for i,n in enumerate(range(1,10)):
   # print(i,n)

my_list =['a','b','c']

#turns the list into an enumerated object, which pairs each item with its index.for example [(0,'a')(1.'b')(2,'c')]
my_tuple =list(enumerate(my_list))

print(my_tuple[2][0])

