# You will have to make a program that checks if a number is odd, even or zero.
# The program will accept only one parameter, an integer.

import sys


def main():
    argv = sys.argv
    if (len(argv)) > 2:
        exit("ERROR")
    elif (len(argv) == 1):
        exit()
    if (not argv[1].isnumeric()):
        exit("ERROR")
    num = int(argv[1])
    if (num == 0):
        print("I'm Zero.")
    elif (num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
