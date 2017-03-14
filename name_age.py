"""Enter your age and name, find out what year you will turn 100."""
from datetime import datetime


def validate_age(s):
    """Validate user input can be converted to int."""
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate_year(age):
    """Calculate year in which user will turn 100."""
    diff = 100 - int(age)
    date = datetime.now()
    year = diff + date.year

    return year




def main():
    """Main project function."""
    name = input("What is your name?  ")
    usr_age = input("How old are you?  ")

    while not validate_age(usr_age):
        usr_age = input(usr_age + " is not a valid input, please enter your age in years.  \
        E.g. 29  ")

    print("Alright {0}, I see you are {1} years old".format(name, usr_age))
    print("You will turn 100 years old in the year {0}".format(calculate_year(usr_age)))

main()

