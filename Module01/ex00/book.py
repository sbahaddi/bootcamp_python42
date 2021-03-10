from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = self.set_name(name)
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def set_name(self, name):
        if not isinstance(name, str):
            exit("name must be a string")
        return name

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for r in self.recipes_list["starter"]:
            if r.name.lower() == name.lower():
                print(r)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for r in self.recipes_list["starter"]:
            if r.recipe_type.lower() == recipe_type.lower():
                print(r)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if recipe in self.recipes_list["starter"]:
            exit("Recipe already exist")
        elif recipe in self.recipes_list["lunch"]:
            exit("Recipe already exist")
        elif recipe in self.recipes_list["dessert"]:
            exit("Recipe already exist")
        if not isinstance(recipe, Recipe):
            exit("The argument must be a recipe.")
        self.recipes_list[recipe.recipe_type.lower()].append(recipe)
