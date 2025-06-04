'''The program will choose a secret word and we'll show
the player only a series of dashes that represent the number of letters in the word. In each
turn, the player must choose a letter: if that letter is in the hidden word, the system will show
where it is located, but if the player chooses a letter that is not in the hidden word, they lose
a life.
In the real hangman game, each time we lose a life, the drawing of the hangman is completed
limb by limb. But in our case, as we still do not have the graphic elements, we will simply tell
the user that they have six lives, and we will deduct them one by one for each time the player
chooses an incorrect letter.'''
import random
word_list =['fairy','hairy','dairy','chrome','rome']
secret_word =random.choice(word_list)


def represent_secretword(word):
    word_in_dashes = []
    for n in word:
        word_in_dashes.append('_')
    return f'secret word is :{('_')* len(word_in_dashes)}'
print(represent_secretword(secret_word))

def asking_to_guess():
    tries = 6
    revealed_letters=['-'for n in secret_word]#list comprehension to showing "-" for letters in the secret_word.once correct letter is guess.this variable is updated automatically
    guessed_letters=[] #previously correctly guessed letters
    while tries>0 and '-'in revealed_letters:

        guessed_letter= input('Guess the letters in the secret word:').lower()
        if guessed_letter in guessed_letters: #check to see if the newly guessed letter is already guessed previously
            print("you aleady guessed that letter.Try a new one!!")
            continue
        else:
            guessed_letters.append(guessed_letter) #if the new letter is not previously guesed,appened the guessed_letter list

        for index,letter in enumerate(secret_word) :# use enumerate to know the index of the letter position
            if letter==guessed_letter:
                revealed_letters[index]=guessed_letter # if the guessed letter is equal to the letter in the secret_word , that guessed letter will be stored in the correct position of the revelated_letters list

        if guessed_letter not in (secret_word):#check to see if guess letter is not in the secret word.if it not in the secret word, reduce one "try"
            tries =tries-1
            print(f'you entered wrong letter.you have only {tries} lifes left!!')


        print (''.join(revealed_letters))#join the strings together without spaces between letters.because now the list is having relvelaed letters like this['f','-','i','-','-'].now we want to show the player what he has guss like this --->> f-i--

        if tries==0 and '-' in revealed_letters:
            print(f'Sorry!! You lost the game.because you ran out of lives.The secret word is: {secret_word} ')

        if '-'not in (revealed_letters):
            print(f'congratulation you won.The secret word is : {''.join(revealed_letters)}')



asking_to_guess()






