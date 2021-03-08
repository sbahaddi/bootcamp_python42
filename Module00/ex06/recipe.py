"""
It is time to discover Python dictionaries. Dictionaries are collections that contain mappings of unique keys to
values.

Hints: check what is a nested dictionary in Python.

First, you will have to create a cookbook dictionary called cookbook.
cookbook will store 3 recipes:
• sandwich
• cake
• salad

Each recipe will store 3 values:
• ingredients: a list of ingredients
• meal: type of meal
• prep_time: preparation time in minutes

Sandwich’s ingredients are ham, bread, cheese and tomatoes. It is a lunch and it takes 10 minutes of preparation.
Cake’s ingredients are flour, sugar and eggs. It is a dessert and it takes 60 minutes of preparation.
Salad’s ingredients are avocado, arugula, tomatoes and spinach. It is a lunch and it takes 15 minutes of
preparation.

1. Get to know dictionaries. In the first place, try to print only the keys of the dictionary. Then only the
values. And to conclude, all the items.
2. Write a function to print a recipe from cookbook. The function parameter will be: name of the recipe.
3. Write a function to delete a recipe from the dictionary. The function parameter will be: name of the recipe.
4. Write a function to add a new recipe to cookbook with its ingredients, its meal type and its preparation
time. The function parameters will be: name of recipe, ingredients, meal and prep_time.
5. Write a function to print all recipe names from cookbook. Think about formatting the output.
6. Last but not least, make a program using the four functions you just created. The program will prompt the
user to make a choice between printing the cookbook, printing only one recipe, adding a recipe, deleting a
recipe or quitting the cookbook.

It could look like the example below but feel free to organize it the way you want to:

> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> 3
Please enter the recipe's name to get its details:
>> cake
Recipe for cake:
Ingredients list: ['flour', 'sugar', 'eggs']
To be eaten for dessert.
Takes 60 minutes of cooking.

Your program must continue running until the user exits it (option 5):
> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> 5
Cookbook closed.

The program will also continue running if the user enters a wrong value. It will prompt the user again until the
value is correct:
> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> test
This option does not exist, please type the corresponding number.
To exit, enter 5.
>>
"""

cookbook = {
    "sandwich": {"ingredients": ["ham", "bread", "tomatoes"], "meal": "lunch", "prep_time": 10},
    "cake": {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
    "salad": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15},
}


def print_recipe(recipe):
    if not recipe in cookbook:
        print("recipe not found")
        return
    print(f"Recipe for {recipe}:")
    print(f'Ingredients list: {cookbook[recipe]["ingredients"]}')
    print(f"To be eaten for {cookbook[recipe]['meal']}.")
    print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.")


def del_recipe(recipe):
    if not recipe in cookbook:
        print("recipe not found")
        return
    del cookbook[recipe]


def all_recipe():
    i = 1
    print("List of all recipes in the cookbook :")
    for key in cookbook:
        print(f"{i}) {key}")
        i += 1


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {"ingredients": ingredients,
                      "meal": meal, "prep_time": prep_time}


def program(choice):
    print("\n")
    if choice == "1":
        name = input("recipe name ?\n")
        if name in cookbook:
            print("recipe already exist\n")
            return
        ingredients = []
        ing = input(
            "ingredient ? enter once to add ingredient, twice once finished\n")
        while (len(ing) > 0):
            ingredients.append(ing)
            ing = input()
        meal = input("meal type ?\n")
        prep_time = input("preparation time ?\n")
        add_recipe(name, ingredients, meal, prep_time)
    elif choice == "2":
        del_recipe(input("name of the recipe to delete\n"))
    elif choice == "3":
        print_recipe(input("recipe name ?\n"))
    elif choice == "4":
        all_recipe()
    elif choice == "5":
        exit("Cookbook closed.")
    else:
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
    print("\n")


def main():
    while (1):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        choice = input("")
        program(choice)
        input("Press enter to continue.")


if __name__ == "__main__":
    main()
