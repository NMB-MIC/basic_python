# cars = ['audi','bmw','subaru','toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())    
# #print(car)

#conditional test

#ture
# car = 'bmw'
# print(car == 'bmw')

# #false
# car = 'audi'
# print(car == 'bmw')


# car = 'Audi'
# print(car == 'audi')
# print(car.lower() == 'audi')
# print(car)

# # print(car != 'audi')


# #numberical
# age = 18
# print(age == 18)
# print(age < 21)
# print(age <= 21)
# print(age > 21)
# print(age >= 21)



# #multiple conditions
# age_0 = 22
# age_1 = 18

# print(age_0 > 21 and age_1 >= 20)
# print(age_0 > 21 or age_1 >= 20)

#check in lists 
requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

#check not in lists
banned_users = ['andrew','carolina','david']
user = 'marie'
print(user not in banned_users)

if user not in banned_users:
    print(f"{user.title()}, you can login")

#Boolean Expressions
game_active = True
game_active = False