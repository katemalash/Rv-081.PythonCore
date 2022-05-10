"""
Suppose you are a cook and you have a lot of lettuce so you've decided to add it to 
all the dishes.
Create a few collections that contain the ingredients of dish; create function that
outputs the ingredients of each dish. Create decoratorr that adds lettuce to all the
dishes.
"""


def recipe_ingredients(let):
    def adding(*dish):
        for i in dish:
            for a in i:
                print(a)
            let()
            print(10*"-")
    return adding


@recipe_ingredients
def lettuce():
    print("lettuce")

sandwich = ["Bread", "Ham", "Cheese", "Tomato"]
pasta = ["Sour cream", "Chiken", "Tomato", "Crackers"]
burger = ["Bride", "Souse BBQ", "Beaf", "Cheese"]
pizza = ["Salami", "Tomato", "Sour cream", "Basil"]

lettuce(sandwich, pasta, burger, pizza)

