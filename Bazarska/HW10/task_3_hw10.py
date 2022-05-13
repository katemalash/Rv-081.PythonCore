#Suppose you are a cook and you have a lot of lettuce so you’ve decided to add it to all the dishes. 
# Create a few collections that contain the ingredients of dish; create function that outputs the ingredients of each dish.
# Create decorator that adds lettuce to all the dishes.
def lettuce(func):
    def add_lettuce(*args):
        func(*args)
        print('lettuce')
    return add_lettuce

@lettuce 

def dishes(dish):
    dish = dish.split(', ')

    for ingrd in dish:
        print(ingrd)

pizza = 'dough, tomato sauce, mozzarella, basil'
tuna_salad = 'tuna, cherry tomatoes, olive oil, red onion'
bruschetta = 'chiabatta, tomatoes, olive oil, oregano'

dishes(bruschetta)
