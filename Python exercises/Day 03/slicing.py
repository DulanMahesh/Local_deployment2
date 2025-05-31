
text ="ABCDEFGHIKLM"
fragment= text[2]
print (fragment)

#extracting fragment of a word using slicing
fragment= text[2:5]# slice start from index 2(including index2 and slice upto index5 but not including index5)
print (fragment)

fragment= text[2:]# slice start from index 2(including index2 and upto the last index)
print (fragment)

fragment= text[:5]# slice start from index 0(including index 0 and slice upto the index 5 but notincluding index 5)
print (fragment)

fragment= text[2:10:2]# slice start from index 2(including index2 and slice upto index 10 but not including index10.the third index tells how many charecters it should count from the previous one to extract the next one)
print (fragment)

fragment= text[::3]# get the number from index 0 to the last index but skipping 3 by 3 when selecting the next charecter to pick
print (fragment)

fragment= text[::-1]# we can obtain the whole chain of charecters.but in reverse(inverse)order one by one
print (fragment)

fragment= text[::-2]# we can obtain the whole chain of charecters.but in reverse(inverse)order two by two(skipping one charecter in each selection)
print (fragment)