"""
kata04
( 0, 4, 132.42222, 10000, 12345.67)
Given the tuple above, return the following result:
> python kata04.py
day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
"""


def main():
    t = (1, 4, 132.42222, 10000, 12345.67)
    print("day_%02d, ex_%02d, %.2f, %.2e, %.2e" % t)


if __name__ == "__main__":
    main()
