# main list for users
# name age, security level with validation
# save the user in current list
# ask if the user wants to continue
# summary

users = []  # start with blank users
security = ["Bad", "Bad", "Good", "Good", "Excellent"]  # 1 2 3 4 5

# loops the whole thing
while True:
    # loops the name
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Invalid. Must be a letter with no space.")

    # loops the age
    while True:
        ageInput = input("Enter your age: ")
        # age validation
        if ageInput.isdigit():
            age = int(ageInput)
            if age >= 0 and age <= 100:
                print("Age valid.")
                break
            else:
                print("Invalid age. Must be between 0 and 120.")
        else:
            print("Invalid. Must be a number.")

    # loops the security level
    while True:
        securityLevelInput = input("Enter your security level: ")
        if securityLevelInput.isdigit():
            securityLevel = int(securityLevelInput)
            if securityLevel >= 1 and securityLevel <= 5:
                status = security[securityLevel - 1]   # status = new variable;  security = list;  securityLevelInput = inputted variable;  - 1 for indexing
                break
            else:
                print("Invalid. Must be a number from 1-5.")
        else:
            print("Invalid. Must be a number.")

    # temporary list 0   1    2              3
    currentUser = [name, age, securityLevel, status]
    users.append(currentUser)

    # ask if adding another user
    if input("Continue? y/n: ").lower() != 'y':
        break
print("*"*50)
print("Registered Users")
print("*"*50)
print("")
for u in users:
    print(f"User: {u[0]} | Age: {u[1]} | Security: {u[2]} | Status: {u[3]}")