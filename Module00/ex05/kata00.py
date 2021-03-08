"""
kata00
t = (19,42,21)
Including the tuple above in your file, write a program that dynamically builds up a formatted string like the
following:
> python kata00.py
The 3 numbers are: 19, 42, 21
"""


def main():
    t = (19, 42, 21)
    s = ", ".join(map(str, t))
    print(f"The {len(t)} numbers are : {s}")


if __name__ == "__main__":
    main()
