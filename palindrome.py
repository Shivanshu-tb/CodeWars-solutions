'''
Write a function that checks if a given string (case insensitive) is a palindrome.
'''

def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word
