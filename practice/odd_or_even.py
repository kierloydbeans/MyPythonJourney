while True:
    # validate input
    numInput = input("Enter a number: ")
    if not numInput.isdigit():
        print("Invalid. Must be a number.")
        continue

    # convert to int
    num = int(numInput)
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

    # continue or no
    con = input("Do you want to continue? (1 if yes, any other character if no): ")
    if con == "1":
        continue
    print("Thank you!")
    break