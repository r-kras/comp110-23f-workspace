"""EX02- One Shot secret_wordle - The second iteration of secret_wordle with one chance to guess."""

__author__ = "730699792"

# choose secret word
# length of secret
# user guess
secret_word : str = "python"
secret_word_length : int = len(secret_word)
guess : str = input(f"What is your {secret_word_length}-letter guess? ")
# redo guess until it is length 6
while (len(guess) != secret_word_length):
    guess = input(f"That was not {secret_word_length} letters! Try again: ")


# box emojis
# empty string for colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
box_string: str = ""


# iterate through characters in guess
i: int = 0
while (i < secret_word_length):
# if character is same type and pos: add green
    if (secret_word[i] == guess[i]):
        box_string += GREEN_BOX
    else:

# if character is not same pos...
# see if its present somewhere in secret
        in_secret: bool = False
        j: int = (i + 1) % secret_word_length
        while (in_secret == False and j != i):
            if (secret_word[j] == guess[i]):
                in_secret = True
            j = (j + 1) % secret_word_length
# if char is present somewhere: add yellow
        if (in_secret == True) :
            box_string += YELLOW_BOX
# if not present anywhere: add white
        else:
            box_string += WHITE_BOX
    i+=1


# print the string of colored boxes
print (box_string)
# if the guess is the same as the secret...
if (guess == secret_word):
    print("Woo! You got it!")
# if not
else:
    print("Not quite. Play again soon!")