# main list for users
# name age, security level with validation
# save the user in current list
# ask if the user wants to continue
# summary

users = []  # start with empty list
security = ["Bad", "Bad", "Good", "Good", "Excellent"]  # list for the security level status
while True:  # loops the whole thing
    while True:  # asks and loops the name
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Must be a letter.")

    while True:  # asks and loops the age
        ageInput = input("Enter your age: ")
        if ageInput.isdigit():
            age = int(ageInput)
            break
        print("Must be a number.")

    while True:
        securityLevelInput = input("Enter the security level: ")
        if securityLevelInput.isdigit():
            securityLevel = int(securityLevelInput)
            if securityLevel >= 1 and securityLevel <= 5:
                # new declared variable      # list  # inputted variable minus 1 for indexing
                status =                     security[securityLevel - 1]
                break
            else:
                print("Must be 1-5")
        else:
            print("Must be a number.")

    current_user = [name, age, securityLevel, status]  # temporary list
    users.append(current_user)  # adds to the users list

    # ask if looping again
    if input("Continue? (y/n): ").lower() != 'y':
        break

# summary
print("Registered Users")

for u in users:
    print(f"User: {u[0]} | Age:{u[1]} | Security: {u[2]} - {u[3]}")
    # index for     user         age              s level   s status
    # indexing is key for lists

# time spent: 35:05.70
# with help of AI, but I did comments to help e understand the code
