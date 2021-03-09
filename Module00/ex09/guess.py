"""
You will have to make a program that will be an interactive guessing game. It will ask the user to guess a
number between 1 and 99. The program will tell the user if their input is too high or too low. The game ends
when the user finds out the secret number or types exit.
You will have to import the random module with the randint function to get a random number. You have to
count the number of trials and print that number when the user wins.
Example:
> python guess.py
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
What's your guess between 1 and 99?
>> 54
Too high!
What's your guess between 1 and 99?
>> 34
Too low!
What's your guess between 1 and 99?
>> 45
Too high!
What's your guess between 1 and 99?
>> A
That's not a number.
What's your guess between 1 and 99?
>> 43
Congratulations, you've got it!
You won in 5 attempts!
If the user discovers the secret number on the first try, tell them. Bonus: if the secret number is 42, make a
reference to Douglas Adams.
> python guess.py
What's your guess between 1 and 99?
>> 42
The answer to the ultimate question of life, the universe and everything is 42.
Congratulations! You got it on your first try!
Other example:
> python guess.py
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
What's your guess between 1 and 99?
>> exit
Goodbye!

"""

import random


def main():
    guess = random.randint(1, 99)
    attempts = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    while(1):
        number = input("What's your guess between 1 and 99?\n")
        if not number.isnumeric() and number.lower() != "exit":
            exit("That's not a number.")
        elif not number.isnumeric() and number.lower() == "exit":
            exit("Goodbye!")
        number = int(number)
        if number > guess:
            print("Too high!")
            attempts += 1
        elif number < guess:
            print("Too low!")
            attempts += 1
        elif number == guess:
            if number != 42:
                print("Congratulations, you've got it!")
                if attempts == 0:
                    print("Congratulations! You got it on your first try!")
                else:
                    print(f"You won in {attempts} attempts!")
            else:
                print(
                    "The answer to the ultimate question of life, the universe and everything is 42.")
                if attempts == 0:
                    print("Congratulations! You got it on your first try!")
                else:
                    print(f"You won in {attempts} attempts!")
            return


if __name__ == "__main__":
    main()
