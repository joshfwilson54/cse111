"""
Josh Wilson
CSE111
Week 2 Project, Passwords.py

For my above and beyond in this assignment, I created a password generator. It defaults to 10 characters but can be changed later if wanted.

1. create lists of different characters we use in passwords. Create a list of those lists.
2. word_in_file: compares if (word) is in (filename) returns bool
3. word_has_character: checks if (word) has a character in a (character_list) returns bool
4. word_complexity: scores (word) based on how many different types of (character_lists) its in. Returns int.
5. password_strength: scores how complex (password) is with above functions. returns [int(complexity score), str(a message explaining why)]
6. generate_password: assumes (character_list) is a list different character lists. generates a password with random characters in those lists. Default length = 10.
7. main: runs password_strength(), generate_password(), or breaks loop and quits.
"""
import random as r

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

complexity_lists = [LOWER, UPPER, DIGITS, SPECIAL]

def word_in_file(word, filename, case_sensitive=False):
    # Open filename as file. check each line and compare if the word entered is in it.
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line_cleaned = line.strip()
            if word.lower() == line_cleaned and case_sensitive is False:
                return True
            elif word == line_cleaned and case_sensitive is True:
                return True
        return False

def word_has_character(word, character_list):
    # Check every character in word, if character is in character_list, return True. Else False.
    for character in word:
        if character in character_list:
            return True
    return False

def word_complexity(word, lists):
    # Create a list for which compares all our variables.
    complexity = 0

    # word_in_file every list and add to our complexity rating
    for complexity_list in lists:
        if word_has_character(word, complexity_list):
            complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    # evaluate given password with functions listed above. Return a strength value and a comment in a list.
    strength_score = 1
    if word_in_file(password, "wordlist.txt"):
        strength_score = 0
        return [strength_score, "Password is a dictionary word and is not secure."]
    if word_in_file(password, "toppasswords.txt", True):
        strength_score = 0
        return [strength_score, "Password is a commonly used password and is not secure."]
    if len(password) < min_length:
        strength_score = 1
        return [strength_score, "Password is too short and is not secure"]
    if len(password) > strong_length:
        strength_score = 5
        return [strength_score, "Password is long, length trumps complexity this is a good password"]
    
    strength_score += word_complexity(password, complexity_lists)
    return [strength_score, "Good password"]

def generate_password(character_list, length=10):
    # select random characters random is used here.
    generated_password = ""
    for x in range(length):
        randomized_list = character_list[r.randint(0 , len(character_list) - 1)]
        generated_password += randomized_list[r.randint(0 , len(randomized_list) - 1)]
    return generated_password

def main():
    while True:
        user_pass = input("Enter your suggested password:\nType 'Q' to quit. Type 'G' to generate a random password.\n")

        if user_pass.lower() == "q":
            break
        elif user_pass.lower() == "g":
            print(generate_password(complexity_lists))
        else:
            p_strength = password_strength(user_pass)
            # list index in order to create a decent format. Next time I will use a dictionary.
            print(f"{p_strength[1]}\nYour password score is {p_strength[0]}")

main()