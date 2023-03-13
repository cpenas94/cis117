from module_lab3_Penas_Trujillo import *

while True:
    user_input = input("Enter a word or sentence (type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    print(f"'{user_input}' is:")
    print(f"- a palindrome: {is_palindrome(user_input)}")
    print(f"- a pangram: {is_pangram(user_input)}")
    print(f"- a tautogram: {is_tautogram(user_input)}")
    print(f"- an isogram: {is_isogram(user_input)}")
    print(f"- an abecedarian: {is_abedecerian(user_input)}")
    print(f"- a dobloon: {is_dobloon(user_input)}")
