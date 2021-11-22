#list in dic

#makeing pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','cheese']
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza")

for topping in pizza['toppings']:
    print(f"\tadding: {topping}")
