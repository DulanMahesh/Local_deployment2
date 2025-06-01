
#excercise2
'''Write a function (you can name it whatever you want)
 that takes any word as a parameter, and returns all of its
 unique letters (without repetition) in alphabetical order.
For example, if when calling this function we pass the word"entertaining", it should return ['a', 'e', 'g', 'i', 'n', 'r', 't']
'''

def whatever(my_word):
    word=[]
    for n in my_word:
        word.append(n)
        repetition_removed= set(word) # to remove repetitions from the list
        sorted_word =sorted(repetition_removed) # to sort the list
    print(sorted_word)
whatever('entertaining')

