pizzas = ['tomato','onion','olives']
friends_pizzas = pizzas[:]
pizzas.append('garlic')
friends_pizzas.append('pepperoni')
print('My favourite pizzas are ')
for pizza in pizzas:
 print(pizza)
print('My friends favourite pizzas are ')
for pizza in friends_pizzas:
 print(pizza)