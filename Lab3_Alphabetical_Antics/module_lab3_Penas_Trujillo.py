# CIS-117 Lab 3
# Module to test alphabetical antics (or word play)
# Group: 3
# Authors: Henry Penas, Fernando Trujillo

def is_palindrome(word):
    """
    Palindrome: a word or sentence that reads the same backwards
    Returns true if input is a Palindrome, otherwise returns false if not.
    """
    word = ''.join(filter(str.isalpha, word)).lower()
    return word == word[::-1]


def is_pangram(sentence):
    """
    Pangram: a phrase or sentence containing all 26 letters of the alphabet
    Returns true if input is a Pangram, otherwise returns false if not.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True


def is_tautogram(sentence):
    """
    Tautogram: a text in which all words start with the same letter
    Returns true if input is a Tautogram, otherwise returns false if not.
    """
    words = sentence.split()
    first_char = words[0][0].lower()
    for word in words:
        if word[0].lower() != first_char:
            return False
    return True


def is_isogram(word):
    """
    Isogram: a word in which no letter of the alphabet occurs more than once
    Returns true if it input is a Isogram, otherwise returns false if not.
    """
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True


def is_abedecerian(word):
    """
    Abedecerian: a word in which the letters appear in alphabetical order
    Returns true if input is a Abedecerian, otherwise returns false if not.
    """
    sorted_word = ''.join(sorted(word.lower()))
    return sorted_word == word.lower()


def is_dobloon(word):
    """
    Dobloon: a word in which every letter that appears in the word appears exactly twice
    Returns true if input is a Dobloon, otherwise returns false if not.
    """
    for letter in word:
        if word.count(letter) != 2:
            return False
    return True
