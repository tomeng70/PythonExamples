# import the random number library so we can randomize the word.
import random

from os import system, name

# create a list of words that the program can choose from.
list_of_words = ["apple", "bicyle", "chemical", "delicate", "evergreen", "freedom", 
                 "gargoyle", "skateboard", "cheese", "physics", "bright", "kangaroo",
                 "container", "wheel", "bicycle", "instrument", "broadcast",
                 "zebra", "zygote", "lever", "inclination", "zoology", "mythology", "biology"]

# index for list_of_words should range from 0 to length of the list minus 1.
max_index = len(list_of_words) - 1
index = random.randint(0, max_index)
word = list_of_words[index]

# the list called "guesses" keeps track of the guesses that the user made so far.
# the list starts out as an empty list.
guesses = []

# the flag "done" is ued to indicate when the user is done playing.
done = False

# give the user a limited number of chances to guess incorrectly.
# use mistakes to track how many mistakes they made.
mistakes = 0
max_mistakes = 6

# game loop.  loop until done.
while not done:
    # loop through the letters of the word.
    # if the current letter has been used as a guess already,
    # then show the letter in the display.
    print("Secret word:", end = " ")
    for letter in word:
        # is the current letter in the guesses list?
        if letter.lower() in guesses:
            # show the letter to the user and terminate the print statement
            # with a space character instead of a newline.
            print (letter, end=" ")
        else:
            # the current letter has not yet been guessed.
            # display it as an underscore.
            print("_", end=" ")
    print(" ")
    
    # tell the user how many mistakes they made and how many they have left.
    print(f"({mistakes} of {max_mistakes} mistakes made)")

    # ask the user to guess a letter
    # use a formatted string to let user know how many mistakes
    # they have made so far.

    guess = input("Please guess a letter: ")
    
    # if they already used this letter, let them know and make them guess again.
    if guess in guesses:
        print(f"You have used the letter '{guess}' already!  Choose a different letter.")
        # jump to the next iteration of the loop.
        continue;
    
    # add the current guest to the list of guesses.
    guesses.append(guess.lower())

    # does the current guess not appear in the secret word?
    # if not, increase the number of mistakes.
    if guess.lower() not in word.lower():
        # current guess does not appear in the secret word.
        # increase the number of mistakes.
        mistakes = mistakes + 1
    
    # check number of mistakes made
    if (mistakes == max_mistakes):
        print("You've made too many mistakes!")
        break

    # loop through each letter of our secret word to see if there are
    # any unguessed letters left.
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            # we still have some unguessed letters in our secret word.
            # the user is not yet done guessing.
            done = False

# after they are done looping check to see if the done flag is true.
# if so, all of the letters in the word were guessed successfully.
if done:
    print(f"Congratulations, you successfully guessed the secret word: {word}")
else:
    print(f"Game over.  The secret word was {word}")
        
        
    