
# CIS-117 Lab 3
# Module to test alphabetical antics (or word play)
# Group: 3
# Authors: Henry Penas, Fernando Trujillo

"""
This module contains functions to test different types of word play:
- Palindrome: a word or sentence that reads the same backwards
- Pangram: a phrase or sentence containing all 26 letters of the alphabet
- Tautogram: a text in which all words start with the same letter
- Isogram: a word in which no letter of the alphabet occurs more than once
- Abedecerian: a word in which the letters appear in alphabetical order
- Dobloon: a word in which every letter that appears in the word appears exactly twice

"""


def is_palindrome(word):
    word = ''.join(filter(str.isalpha, word)).lower()
    return word == word[::-1]


def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True


def is_tautogram(sentence):
    words = sentence.split()
    first_char = words[0][0].lower()
    for word in words:
        if word[0].lower() != first_char:
            return False
    return True


def is_isogram(word):
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True


def is_abedecerian(word):
    sorted_word = ''.join(sorted(word.lower()))
    return sorted_word == word.lower()


def is_dobloon(word):

    for letter in word:
        if word.count(letter) != 2:
            return False
    return True
