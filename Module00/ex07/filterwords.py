"""
Using list comprehensions, you will have to make a program that removes all the words in a string that are
shorter than or equal to n letters, and returns the filtered list with no punctuation.
The program will accept only two parameters: a string, and an integer n.
Example:
> python filterwords.py "Hello, my friend" 3
['Hello', 'friend']
> python filterwords.py "A robot must protect its own existence as long as such protection
,→ does not conflict with the First or Second Law" 6
['protect', 'existence', 'protection', 'conflict']
> python filterwords.py Hello World
ERROR
> python filterwords.py 300 3
ERROR
"""

import sys
import string
import re


def main():
    args = sys.argv
    del args[0]
    if len(args) == 2 and not args[0].isnumeric() and args[1].isnumeric():
        args[0] = re.sub(r'[^\w\s]', '', args[0])
        splited = args[0].split(" ")
        result = [str for str in splited if len(str) > int(args[1])]
        print(result)
    else:
        exit("ERROR")


if __name__ == "__main__":
    main()
