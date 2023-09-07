"""EX01- Chardle - the game Wordle without visuals"""

__author__ = "730699792"


# Recieve 5-letter word from user
user_word: str = input("Enter a 5-character word: ")
# If word is not 5 letters, end the program
if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

# Recieve single character from user
user_guess: str = input("Enter a single character: ")
# If a character was not inputted, end the program
if (len(user_guess) != 1):
    print("Error: Character must be a single character")
    exit()

# Initialize a count variable
char_count: int = 0;
print("Searching for " + user_guess + " in " + user_word)
# If character found at the first space
if(user_word[0] == user_guess):
    print(user_guess + " found at index 0")
    char_count += 1
# If character found at the second space
if(user_word[1] == user_guess):
    print(user_guess + " found at index 1")
    char_count += 1
# If character found at the third space
if(user_word[2] == user_guess):
    print(user_guess + " found at index 2")
    char_count += 1
# If character found at the fourth space
if(user_word[3] == user_guess):
    print(user_guess + " found at index 3")
    char_count += 1
# If character found at the fifth space
if(user_word[4] == user_guess):
    print(user_guess + " found at index 4")
    char_count += 1

# Print out number found
if (char_count == 0):
    print("No instances of " + user_guess + " found in " + user_word)
else: 
    print(str(char_count) + " instances of " + user_guess + " found in " + user_word)