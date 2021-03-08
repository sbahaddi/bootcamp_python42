# Create a function called text_analyzer that displays the sums of upper-case characters, lower-case characters,
# punctuation characters and spaces in a given text.
# text_analyzer will take only one parameter: the text to analyze. You have to handle the case where the text is
# empty (maybe by setting a default value). If there is no text passed to the function, the user is prompted to give
# one.

import string


def analyze(text):
    print(f"The text contains {len(text)} characters:")
    print(f"- {sum(1 for c in text if c.isupper())} upper letters")
    print(f"- {sum(1 for c in text if c.islower())} lower letters")
    print(f"- {sum(1 for c in text if c in string.punctuation)} punctuation marks")
    print(f"- {sum(1 for c in text if c == ' ')} spaces")


def text_analyzer(text="", *other):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if other:
        exit("ERROR")
    if (len(text) == 0):
        analyze(input("What is the text to analyse? \n"))
    else:
        analyze(text)


if __name__ == "__main__":
    text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
