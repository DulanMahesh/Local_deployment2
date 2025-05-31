my_text ="Hello Boys whaggth up"
result=my_text[0]
print(result)

#index method (search from left to right)
result =my_text.index("h") ## want to find the position of the "h" from left to right and gives the index of first "h" it sees
print(result)

#rindex method (search from right to left)
result=my_text.rindex("h")# want to find the position of the "h" from right to left and gives the index of first "h" it sees
print(result)

result=my_text.index("h",13)# search for the "h" begin from index 13
print(result)

result=my_text.index("h",11,14)# search for the "h" begin from index 11 to index 14
print(result)

word = "computer"
print (word[5])


