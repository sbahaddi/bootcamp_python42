"""
You will have to make a program that prints the results of the four elementary mathematical operations
of arithmetic (addition, subtraction, multiplication, division) and the modulo operation. This should be
accomplished by writing a function that takes 2 numbers as parameters and returns 5 values, as formatted in
the console output below.
"""

import sys


def add(a, b):
    return (a + b)


def diff(a, b):
    return (a - b)


def prod(a, b):
    return (a * b)


def div(a, b):
    if b == 0:
        return ("ERROR (div by zero)")
    return (a/b)


def mod(a, b):
    if b == 0:
        return ("ERROR (modulo by zero)")
    return(a % b)


def usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("     python operations.py 10 3")


if __name__ == "__main__":
    argv = sys.argv
    del(argv[0])
    if (len(argv) == 0):
        usage()
    elif (len(argv) > 2):
        print("InputError: too many arguments\n")
        usage()
    elif (not argv[0].isnumeric() or not argv[1].isnumeric()):
        print("InputError: only numbers\n")
        usage()
    else:
        a = int(argv[0])
        b = int(argv[1])
        ljust = 12
        print(f"{'Sum:'.ljust(ljust)} {add(a,b)}")
        print(f"{'Difference:'.ljust(ljust)} {diff(a,b)}")
        print(f"{'Product:'.ljust(ljust)} {prod(a,b)}")
        print(f"{'Quotient:'.ljust(ljust)} {div(a,b)}")
        print(f"{'Remainder:'.ljust(ljust)} {mod(a,b)}")
