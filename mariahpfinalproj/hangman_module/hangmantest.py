
from functions import *

"""
    testIsWinnerTrue()
    test if the IsWinner function works as desired when
    user guesses all characters in the answer
"""
def testIsWinnerTrue():
    isWinner = IsWinner('testanswer', 'tesanwer')
    assert(isWinner == True)

"""
    testIsWinnerFalse()
    test if the IsWinner function works as desired when
    user does not guess all characters in the answer
"""
def testIsWinnerFalse():
    isWinner = IsWinner('testanswer', 'tesnwxg') 
    assert(isWinner == False)   