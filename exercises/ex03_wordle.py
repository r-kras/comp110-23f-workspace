"""A six-turn complete game of wordle."""

__author__ = "730699792"


def contains_char(searched_word: str, target_letter: str) -> bool:
    """A function to determine if a character is present in a string.
    
    Keyword parameters:
    searched_word -- the string being searched
    target_letter -- the character to be found
    """
    # raise assertion error if target_letter is not a single character
    assert len(target_letter) == 1
    # assume character is not in word
    in_secret: bool = False
    j: int = 0
    # iterate through characters of word
    while (j != len(searched_word) and in_secret == False):
        # if letter is found in word, set equal to true
        if (searched_word[j] == target_letter):
            in_secret = True
        j = j + 1
    return in_secret


def emojified(user_guess: str, secret_word: str) -> str:
    """Returns a string of emojis corresponding to similar characters between both strings.

    Keyword Parameters:
    user_guess -- the string guessed that will be iterated through
    secret_word -- the set word that will be used for comparison
    """
    # throw assertion error is the lengths of the inputs are not equal
    assert len(user_guess) == len(secret_word)
    # empty string for colored boxes
    box_string: str = ""
    # box emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # iterate through characters in user_guess
    i: int = 0
    while (i < len(secret_word)):
        # if character is same type and pos: add green
        if (secret_word[i] == user_guess[i]):
            box_string += GREEN_BOX
        elif (contains_char(secret_word, user_guess[i])):
        # if char is present somewhere: add yellow
            box_string += YELLOW_BOX
        # if not present anywhere: add white
        else:
            box_string += WHITE_BOX
        i += 1

    # return the string of colored boxes
    return box_string

def input_guess(string_length: int) -> str:
    """Taking a user input with a specified length.

    Keyword parameters:
    string_length -- the desired length of the input
    """
    # take in user input
    user_guess: str = input(f"Enter a {string_length} character word: ")
    # redo user_guess until it is length 6
    while (len(user_guess) != string_length):
        user_guess = input(f"That was not {string_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    # choose secret word
    # user's guess of the secret word
    # current turn counter
    secret_word: str = "codes"
    user_guess: str = ""
    turn_count: int = 0

    while (user_guess != secret_word and turn_count < 6):
        # increment turn count by 1
        turn_count += 1
        # take in user's guess
        print(f"=== Turn {turn_count}/6 ===")
        user_guess = input_guess(5)
        # print out similar characters emojified
        print(emojified(user_guess, secret_word))    

    # if game ended because before all turns were used
    # print winning statement
    if (secret_word == user_guess):
        print(f"You won in {turn_count}/6 turns!")
    # if game ended because all turns were used
    # print losing statement
    else:
        print("X/6 - Sorry, try again tomorrow!")