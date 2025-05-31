text ="we are Going to learn 6 methods today"
result =text.upper()
print(result)

result =text[4].upper()
print(result)

result =text[7].lower()
print(result)

result =text.split()#split method
print(result)

result =text.split("e")# to use the charcter"e" as the separator
print(result)

#lets check join()

a= 'I'
b= "love"
c='you'
d=" ".join([a,b,c])
print(d)

##use of find()

text2 ="we are Going to learn 6 methods today"

print(text2.find("are")) ## the difference between find() and index , in index if the string or set of charecters that you search is not inside the set of string it will give u error. but find() ony gives you -1 as return

##use of replace()

print(text2.replace("are","WILL"))
####exercise
word_list = ["Simple","is","better","than","complex."]

result =" ".join(word_list)
print(result)
