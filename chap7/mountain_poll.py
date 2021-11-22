responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store the response in the dictionary
    responses[name] = response

    #quit
    repeat = input("Would you like to let another person respond ? (yes/no)")
    if repeat == 'no':
        polling_active = False

#result
print("\n--- Poll Result ---")
for name , response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")