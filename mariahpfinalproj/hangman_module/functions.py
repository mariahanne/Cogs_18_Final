import random

"""
    GetAnswerUnderscores(answer, chars_guessed)
    returns the answer to be printed with the valid guesses,
    and unguessed words shown as an underscore
"""
def GetAnswerUnderscores(answer, chars_guessed):
    newword = ''
    for items in answer:
        if items in chars_guessed:
            newword = newword + items
        else:
            newword = newword + '_'
    return newword

"""
    GetWordWithSpaces(word)
    prints the given word with spaces inbetween
    for visual appeal when guessing
"""
def GetWordWithSpaces(word):
    newword = ''
    for i in range(0, len(word) -1):
        newword = newword + word[i] + " "
    return newword +  word[-1]

"""
    IsWinner(answer, chars_guessed)
    checks if the characters guessed results in a win
    given the answer
"""     
def IsWinner(answer, chars_guessed):
    pass
    count = 0
    for chars in answer:
        if chars in chars_guessed:
            count = count + 1
    return count == len(answer)

"""
    IsGuessValid(current_guess, chars_guessed)
    checks if the guess is an alphabetical value,
    and if the character has already been guessed
"""
def IsGuessValid(current_guess, chars_guessed):
    pass
    if current_guess.isalpha() and len(current_guess) == 1:
        if current_guess not in chars_guessed:
            return True
    return False

"""
    IsGuessCorrect(answer, valid_char_guess)
    checks if the guessed character is in the 
    word answer, then it is correct
"""
def IsGuessCorrect(answer, valid_char_guess):
    for items in answer:
        if items == valid_char_guess:
            return True
    return False

"""
    Play(answer, numStrikes)
    Play one round of hangman
    with the given answer and number of strikes
"""
def Play(answer, numStrikes):
    strike = numStrikes
    chars_guessed = ''
    while strike > 0:
        # print the current guessed characters in the answer, with spaces between underscores 
        print(GetWordWithSpaces(GetAnswerUnderscores(answer, chars_guessed)))

        # get character guess, and set it to uppercase
        guess_char = input("Guess: ").upper()
        
        # check if winner
        if IsWinner(answer, chars_guessed):
            print('Winner!')
            break
        # check if guess is valid    
        if IsGuessValid(guess_char, chars_guessed) and IsGuessCorrect(answer, guess_char):
            print('Nice Guess!')
            chars_guessed = chars_guessed + guess_char

            # check if winner
            if IsWinner(answer, chars_guessed):
                print('Winner!')
                break
            else:
                continue
        # check if the character has already been guessed
        elif guess_char in chars_guessed:
            print('You have already guessed this character.' + guess_char)
        # else the guess is incorrect    
        else:
            strike = strike - 1
            print(guess_char + ' is incorrect. You have ' + str(strike) +  ' strikes remaining.')
    # if on last strike, lose        
    if strike == 0:
        print('Loser! The answer is: ' + answer)