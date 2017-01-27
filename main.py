from recipe_book.recipe_book import RecipeBook

if __name__=="__main__":
    hyperlinks = ["https://www.buzzfeed.com/rachelysanders/genius-three-ingredient-recipes",
    "https://www.buzzfeed.com/peggy/34-insanely-simple-two-ingredient-recipes"]
    # "https://www.buzzfeed.com/lindsayhunt/one-two-three-dessert"
    rb = RecipeBook()
    rb.get_recipes(hyperlinks[0], [1, -2])
    rb.get_recipes(hyperlinks[1],[0, -2])
    print(rb.to_json())
