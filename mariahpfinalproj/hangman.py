import random
from hangman_module.functions import *

wordList = ['BANANA', 'MARIAH', 'CHIHUAHUA', 'HANGMAN', 'CAIFORNIA']
# to start game, pass in the number of strikes and a list of words to pick  from

"""
    StartHangman(numStrikes, word_list)
    the main function of the hangman program. Pass in the number of strikes
    and a list of words, then the program will loop hangman games with random words from the list 
    until user chooses not to play.
""" 
def StartHangman(numStrikes, word_list):
    while True:
        # Get random answer from word list
        answer = random.choice(word_list).upper()
        Play(answer, numStrikes)

        prompt = input('Play again? If yes, type \'y\' or \'Y\' If not: type \'N\' or \'n\'')
        if prompt.lower() != 'y':
            break

StartHangman(5, wordList)