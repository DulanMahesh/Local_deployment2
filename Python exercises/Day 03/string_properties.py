#string properties
name ="Harry"
#name[0]="G" ## there will be an error as the string is immutable

a1="hello"
a2="bigboy"
print(a1+a2) # strings are concatanable

a1="Le"
print(a1*5)# strings are multipliable

print(len(name)) #we can determine the lenghth of the string

sentence="Big boy is mommys boy"
print( "mommys" in sentence)#can check the content of the string
