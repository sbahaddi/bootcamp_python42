"""
You will have to make a function which encodes strings into Morse code.
The input will accept all alphanumeric characters.
Example:
> python sos.py "SOS"
... --- ...
> python sos.py
> python sos.py "HELLO / WORLD"
ERROR
> python sos.py "96 BOULEVARD" "Bessiere"
----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .
"""

import sys


def main():
    MORSE_CODE_DICT = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----."
    }

    args = sys.argv
    if len(args) == 1:
        return
    del args[0]
    args = (" ".join(args)).lower()
    args = args.split(" ")

    for x in args:
        if not x.isalnum():
            exit("ERROR")
    args = "/ ".join(args)
    for l in MORSE_CODE_DICT:
        args = args.replace(l, MORSE_CODE_DICT[l] + " ")
    print(args)


if __name__ == "__main__":
    main()


# ----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .
# ----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .
