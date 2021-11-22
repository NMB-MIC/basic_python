unconfirmed_users = ['alice','brian','candace']
comfirmed_users =[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    comfirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for comfirmed_user in comfirmed_users:
    print(comfirmed_user.title())
