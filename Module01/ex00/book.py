from datetime import datetime


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
