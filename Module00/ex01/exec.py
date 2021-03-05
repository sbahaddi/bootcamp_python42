
# You will have to make a program that reverses the order of a string and the case of its words.
# If we have more than one argument we have to merge them into a single string and separate each arg by a ’ ’
# (space char).

import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        del argv[0]
        argv = " ".join(argv)
        argv = argv.swapcase()
        argv = argv[::-1]
        print(argv)
    else:
        exit()
