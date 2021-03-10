from recipe import Recipe
from book import Book


def main():
    r = Recipe(
        name='Pain',
        cooking_lvl=1,
        cooking_time=15,
        ingredients=['menfou'],
        recipe_type='Starter'
    )

    b = Book("name")
    b.add_recipe(r)
    b.get_recipes_by_types("Starter")
    b.add_recipe(b)


if __name__ == "__main__":
    main()
