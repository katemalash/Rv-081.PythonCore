def recipe_ingredients(func):
    def inner(*recipe):
        for i in recipe:
            for a in i:
                print(a)
            func()
            print(" ")
    return inner


@recipe_ingredients
def lettuce():
    print("lettuce")


recipe_1 = ["loaf", "honey", "cheese"]
recipe_2 = ["sweets", "milk", "flour"]
recipe_3 = ["ham", "salt", "bread", "lamb"]

lettuce(recipe_1, recipe_2, recipe_3)
