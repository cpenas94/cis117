from module_lab3_Penas_Trujillo import *

while True:
    user_input = input("Enter a word or sentence (type 'quit' to exit): ")
    """
    Choice of testing an input or closing the program
    """

    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    """
    Closes the program
    """


"""
Prints whether input for each alphabetical antic is true or false
"""

    print(f"'{user_input}' is:")
    print(f"- Palindrome: {is_palindrome(user_input)}")
    print(f"- Pangram: {is_pangram(user_input)}")
    print(f"- Tautogram: {is_tautogram(user_input)}")
    print(f"- Isogram: {is_isogram(user_input)}")
    print(f"- Abecedarian: {is_abedecerian(user_input)}")
    print(f"- Dobloon: {is_dobloon(user_input)}")
