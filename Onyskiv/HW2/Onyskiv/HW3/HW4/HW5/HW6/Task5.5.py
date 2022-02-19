codeTuple='1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f','g','h','i','j','k','@','$','^','#'

for i in range(10):
 userSymbol=input('Enter symbol:')
 
 entryIndex=codeTuple.index(userSymbol)
 
 print(entryIndex)
print(codeTuple)