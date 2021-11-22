class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

#making an instance
my_dog = Dog('Willi',6)
your_dog = Dog('Lucy',3)

#access attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#calling methods
my_dog.sit()
my_dog.roll_over()

#your dog
#access attributes
print(f"\n\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

#calling methods
your_dog.sit()
your_dog.roll_over()


