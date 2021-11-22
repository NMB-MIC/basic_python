requested_toppings = ['mushrooms','extra cheese','apple']
available_topings = ['mushrooms','pepperoni','extra cheese']

print("Making pizza program\n")
for requested_topping in requested_toppings:
    if requested_topping in available_topings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry, we don't have {requested_topping}")
print("\nfinish making youe pizza!")


# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")

# print("\n finish making youe pizza!")


# print("elif\n\n")
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# elif 'extra chesse' in requested_toppings:
#     print("Adding extra cheese")

