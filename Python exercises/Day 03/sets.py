#one way of creating sets
my_set =set({1,2,3,4,5})
print(type(my_set))
print(my_set)

# second way of create sets

my_set2={1,2,3,4,5}
print(type(my_set2))
print(my_set2)

#my_set2[0] # error gives.indexing is not support in sets
#my_set2[1] =5 # error gives.sets does not support changing elements inside the sets once created

my_set3 =({1,2.5,"gammal",("tuple")}) # sets supports data types,int,string,floats,Tuples.cause those types are immutable.sets does not support lists,dictionaries
print(my_set3)

print(len(my_set3)) # it supports len()function

print(2.5 in my_set3)# it supports queries

s1= {1,2,3}
s2={3,4,5}
s3 =s1.union(s2) #it support union()function
print(s3)

s2.add(19) # sets support adding element
print(s2)
s2.add((57,68,99,789))#lets add a tuple inside the sets
print(s2) # it works

s2.remove(19)# sets supports removing elements
print(s2)

lucky_draw =s2.pop()# removing random number through pop()
print(lucky_draw)

s2.clear()#clear the set
print(s2)
