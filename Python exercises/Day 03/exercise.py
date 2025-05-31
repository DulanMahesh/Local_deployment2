passage = (input("Enter your text:")).lower()
random_letters=(input("Enter three random letters with spaces between them:").lower()).split()
print(type(random_letters))
print(random_letters)

letter_count1 =passage.count(random_letters[0])
letter_count2 =passage.count(random_letters[1])
letter_count3 =passage.count(random_letters[2])

print(f"letter {random_letters[0]} apperars {letter_count1} times")
print(f"letter {random_letters[1]} apperars {letter_count2} times")
print(f"letter {random_letters[2]} apperars {letter_count3} times")

#count the words in the list
words =passage.split() #split the text so we can count them as words['my','name','is','dulan','mahesh','suraweera']
no_of_words =len(words)
print(f"There are {no_of_words} words in this text")
print(f"First letter of the text is {passage[0]} and last letter of the text is {passage[-1]}")#first letter and last letter of the passage

#invert the order of the words
words.reverse() # to reverse the list order
inverted_sentence = " ".join(words) # join the inverted words
print(inverted_sentence)

#Looking for the word "python " in the text

word_exists= "python"in words
dic ={True:'exists',False:'not exists'}##

print(f"The word 'python' {dic[word_exists]} in the text")

