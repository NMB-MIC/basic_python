def make_pizza(*toppings,size):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")

# make_pizza('mushrooms',size=16)
# make_pizza('mushrooms','green peppers','cheese',size=12)