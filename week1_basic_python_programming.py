name = input("Enter your name: ")
age = int(input("How old are you?"))
year = int(input("Input your year level: "))
if year <= 4 and year >= 1:
    grade1 = int(input("Enter first grade: "))
    grade2 = int(input("Enter second grade: "))
    grade3 = int(input("Enter third grade: "))
    grade4 = int(input("Enter fourth grade: "))
    grade5 = int(input("Enter fifth grade: "))

    average = ((grade1 + grade2 + grade3 + grade4 + grade5) / 5)
    rounded_average = (round(average, 2))

    print(f"You are {name}. You are currently in Year {year} and you are {age} years old.")
    print(f"Your grades are {grade1}, {grade2}, {grade3}, {grade4}, {grade5}.")
    print(f"For this semester, you have an average of {rounded_average}.")

    if average >= 95 and average <= 100:
        print("You passed. You got A")
    elif average >= 90 and average <= 94:
        print("You passed. You got B")
    elif average >= 85 and average <= 89:
        print("You passed. You got C")
    elif average >= 80 and average <= 84:
        print("You passed. You got D")
    elif average >= 75 and average <= 79:
        print("You passed. You got E")
    elif average < 75:
        print("You got F. You failed.")
    else:
        print("Invalid input")
else:
    print("Error")