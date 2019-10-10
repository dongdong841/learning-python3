import random
import pics
import words

def get_random_word(word_list):
    index = random.randint(0, len(word_list)-1)
    return word_list[index]

def display_board(missed_letters, correct_letters, secret_word):
    print(pics.HANGMAN_PICS[len(missed_letters)])
    print('')

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print('')

    blanks = '_'*len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters
