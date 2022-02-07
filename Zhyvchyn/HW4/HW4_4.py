R, S, K = [int(x) for x in input('Please enter R S K (radius, area and passage)').split()]
print('Possible') if 2*R <= S** - 2*K else print('Impossible')