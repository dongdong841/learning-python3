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
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print('')

def get_guess(already_guessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    print('Do you want to play again? (yes or not)')
    return input().lower().startswith('y')

print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words.words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = 
