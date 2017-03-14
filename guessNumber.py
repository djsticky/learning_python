import random

def validate_input(string):
    """Check if input is a number."""
    try:
        int(string)
        return True
    except ValueError:
        return False

def main():
    """Main number guessing function."""
    number = random.randint(1, 10)
    guessed = False
    guesses = 0
    usr_guess = input("What number from 1 to 10 am I thinking of?  ")
    while not guessed and guesses < 5:
        if not validate_input(usr_guess):
            usr_guess = input(usr_guess + " isn't a valid number, \
            please choose a number between 1 and 10:  ")
            continue
        else:
            guesses += 1
            if int(usr_guess) > number:
                if not guesses == 5:
                    print(str(5 - guesses) + " guesses remaining")
                    usr_guess = input("To high, try again!  ")
            elif int(usr_guess) < number:
                if not guesses == 5:
                    print(str(5 - guesses) + " guesses remaining")
                    usr_guess = input("To low, try again!  ")
            elif int(usr_guess) == number:
                print("You guessed it in %i guesses!" % guesses)
                guessed = True

    if not guessed and guesses == 5:
        print("Out of guesses, thanks for playing!")


main()