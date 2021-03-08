"""
kata03
phrase = "The right format"
Write a program to display the string above right-aligned with ‘-’ padding and a total length of 42 characters:
> python kata03.py | cat -e
--------------------------The right format%
> python kata03.py | wc -c
42
"""


def main():
    phrase = "The right format"
    print(phrase.rjust(42, '-'), end="")


if __name__ == "__main__":
    main()
