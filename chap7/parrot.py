# message = "Tell me something, "
# message += "and I will repeat it back to you: "

# prompt = input(message)
# print(prompt)


# while True:
#   age = input("How old are you?")
#   age = int(age)
#   print(age>20)

prompt = "How old are you?"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(f"Your answer: {message}") 


# active = True
# while active:
#     message = intput(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

while True:
    message = input(prompt)
    if message =='quit':
        break
    else:
        print(message)
