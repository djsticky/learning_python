"""Check if a user entered number is even or odd."""

def main():
    """Main Function."""
    num = input("Please enter a number:  ")
    check = input("Please enter a number divide into your number:  ")
    mod = float(num) % 2
    multiple = float(num) % 4
    check_mod = float(num) % float(check)

    if mod == 0:
        print(num + " is even")
    else:
        print(num + " is odd")
    if multiple == 0:
        print(num + " is a multiple of 4")
    else:
        print(num + " is NOT a multiple of 4")
    if check_mod == 0:
        print ("{0} divides equally into {1}".format(check, num))
    else:
        print ("{0} does NOT divide equally into {1}".format(check, num))
main()
