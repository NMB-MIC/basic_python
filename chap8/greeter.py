def greet_user():
    print("Hello !")

greet_user()


def greet_user2(username):
    print(f"Hello, {username.title()}")

greet_user2('suraphop')


def greet_user3(username,first='suraphop'):
    print(f"Hello, {username.title()}, your first name is {first}.")

greet_user3('j6638', 'Suraphop')

#position error 
greet_user3('suraphop', 'j6639')

#keyword arguments
greet_user3(username='j6639', first='suraphop')
greet_user3(first='suraphop',username='j6639')

#default values
greet_user3('j6638')
greet_user3('j6638','john')
