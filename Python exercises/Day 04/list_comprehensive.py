#example1
word ="python"
list =[]

for alphabet in word:
    list.append(alphabet)
print(list)


#example 2
feet =[10,20,30,40,50]
meters=[]

for n in feet:
    meters.append(n*0.3048)
print(meters)


#example3

meters=[ f*0.3028 for f in feet]

print(meters)





