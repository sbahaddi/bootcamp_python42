"""
kata02
(3,30,2019,9,25)
Given the tuple above, whose values stand for: (hour, minutes, year, month, day), write a program that
displays it in the following format:
> python kata02.py
09/25/2019 03:30
"""

import datetime


def main():
    date = (3, 30, 2019, 9, 25)
    date = datetime.datetime(date[2], date[3], date[4], date[0], date[1])
    date = date.strftime("%m/%d/%Y %H:%M")
    print(date)


if __name__ == "__main__":
    main()
