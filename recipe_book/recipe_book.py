import json
from recipe_book.utilities import make_soup, strip_list

class RecipeBook:
    def __init__(self):
        self.recipe_book = dict()

    def get_recipes(self, buzzfeed_url, indices):
        self.recipe_book[buzzfeed_url] = dict()
        soup = make_soup(buzzfeed_url)

        html_recipes = soup.find_all("div", class_="buzz_superlist_item")
        relevant_recipes = html_recipes[indices[0]:indices[1]]

        for recipe in relevant_recipes:
            equation = recipe.h2.contents[1]
            desc = recipe.find_all("p", class_="sub_buzz_desc_w_attr")
            url = desc[0].a["href"] if desc and desc[0].a else "NO URL FOUND"
            components = equation.split('=')
            name = components[1].strip() if len(components) > 1 else components[0]
            self.recipe_book[buzzfeed_url][name] = {
                "ingredients" : strip_list(components[0].split('+')),
                "url" : url
            }

    def to_json(self, filename='fixtures/recipe_book.json'):
        return json.dump(self.recipe_book, open(filename, 'w'), indent=4, sort_keys=True)
