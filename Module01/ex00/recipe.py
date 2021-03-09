class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = self.set_name(name)
        self.cooking_lvl = self.set_cooking_lvl(cooking_lvl)
        self.cooking_time = self.set_cooking_time(cooking_time)
        self.ingredients = self.set_ingredients(ingredients)
        self.recipe_type = self.set_recipe_type(recipe_type)
        self.description = description

    def set_name(self, name):
        if not isinstance(name, str):
            exit("Name must be a string")
        return name

    def set_cooking_lvl(self, cooking_lvl):
        if not isinstance(cooking_lvl, int):
            exit("cooking level must be a number")
        return cooking_lvl

    def set_cooking_time(self, cooking_time):
        if not isinstance(cooking_time, int):
            exit("cooking time must be a number")
        return cooking_time

    def set_ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            exit("ingredients must be a list")
        return ingredients

    def set_recipe_type(self, recipe_type):
        if not isinstance(recipe_type, str):
            exit("recipe type must be a string")
        return recipe_type

    def __str__(self):
        string = self.name
        string += "cooking level = " + str(self.cooking_lvl) + "\n"
        string += "cooking time = " + str(self.cooking_time) + ".\n"
        string += "ingredients = " + str(self.ingredients) + ".\n"
        string += "description = " + str(self.description) + ".\n"
        string += "recipe_type = " + str(self.recipe_type) + "."
        return string
