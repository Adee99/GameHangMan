import random
from WordsForGame import WordsForGame
import string


def getValidWord(WordsForGame):
    word = random.choice(WordsForGame)  # randomly chooses words from list
    while '-' in word or ' ' in word:
        word = random.choice(WordsForGame)

    return word.upper()


def hangman():
    word = getValidWord(WordsForGame)
    lettersInWord = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lettersUsed = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(lettersInWord) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(lettersUsed))

        # what current word is (ie W - R D)
        listOfWords = [letter if letter in lettersUsed else '-' for letter in word]
        print('Current word: ', ' '.join(listOfWords))

        lettersInputByUser = input('Guess a letter: ').upper()
        if lettersInputByUser in alphabet - lettersUsed:
            lettersUsed.add(lettersInputByUser)
            if lettersInputByUser in lettersInWord:
                lettersInWord.remove(lettersInputByUser)
                print('')

            else:
                lives = lives - 1  # take away a chance if wrong
                print('\n<---- The letter you entered,', lettersInputByUser, 'is not in the word ---->')

        elif lettersInputByUser in lettersUsed:
            print('\n<---- You have already used that letter. Try with another letter ---->')

        else:
            print('\n<---- The entered letter is not a valid ---->')

    # gets here when len(lettersInWord) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()