LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    # Open filename as file. check each line and compare if the word entered is in it.
    with open(filename) as file:
        for line in file:
            line_cleaned = line.strip()
            if word.lower() == line_cleaned and case_sensitive is False:
                # print("It's in here, case sensitive false.")
                return True
            elif word == line_cleaned and case_sensitive is True:
                # print("It's in here, case sensitive true")
                return True
        # print("Not Found")
        return False

def word_has_character(word, character_list):
    # Check every character in word, if character is in character_list, return True. Else False.
    for character in word:
        if character in character_list:
            # print(f"Character {character} found in {character_list}") DEBUG ONLY.
            return True
    # print(f"No characters in {word} were found in {character_list}") DEBUG ONLY
    return False

def word_complexity(word):
    # Create a list for which compares all our variables.
    complexity_lists = [LOWER, UPPER, DIGITS, SPECIAL]
    complexity = 0

    # word_in_file every list and add to our complexity rating
    for complexity_list in complexity_lists:
        if word_has_character(word, complexity_list):
            if word_has_character:
                complexity += 1
    return complexity

def password_strength(password, min_lenth=10, strong_length=16):
    password_strength = 1
    while True:
        if word_in_file(password, "wordlist.txt"):
            print(f"Password is a dictionary word and is not secure.")
            return password_strength - 1
        if word_in_file(password, "toppasswords.txt", True):
            print("Password is a commonly used password and is not secure.")
            return password_strength - 1

def main():
    while True:
        user_pass = input("Enter your suggested password:\n")

        if user_pass == "q".lower():
            quit()

        password_strength(user_pass, 10, 16)

test_input = input("Enter test word\n")

# print(word_has_character(test_input, UPPER))
# print(word_in_file(test_input, "wordlist.txt", True))
# print(word_complexity(test_input))

password_strength(test_input)