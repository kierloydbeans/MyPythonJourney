name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 120 and age > 1:
    year = int(input("Enter your year level: "))
    if year >= 1 and year <= 4:
        eng = int(input("Enter your english grade: "))
        if eng >= 1 and eng <= 100:
            math = int(input("Enter your math grade: "))
            if math >= 1 and math <= 100:
                sci = int(input("Enter your science grade: "))
                if sci >= 1 and sci <= 100:
                    lang = int(input("Enter your languages grade: "))
                    if lang >= 1 and lang <= 100:
                        prog = int(input("Enter your programming grade: "))
                        if prog >= 1 and prog <= 100:
                            average = ((eng + math + sci + lang + prog) / 5)
                            rounded_average = round(average, 2)
                            if rounded_average >= 75:
                                print(f"Congratulations {name}! You passed.")
                                print("Summary of grades: ")
                                print(f"Math: {math}")
                                print(f"English: {eng}")
                                print(f"Science: {sci}")
                                print(f"Languages: {lang}")
                                print(f"Programming: {prog}")
                                print(f"Average: {rounded_average}")
                                if rounded_average >= 95 and rounded_average <= 100:
                                    print("You got an A.")
                                elif rounded_average >= 90 and rounded_average <= 94:
                                    print("You got a B.")
                                elif rounded_average >= 85 and rounded_average <= 89:
                                    print("You got a C.")
                                elif rounded_average >= 80 and rounded_average <= 84:
                                    print("You got a D.")
                                elif rounded_average >= 75 and rounded_average <= 79:
                                    print("You got an E.")
                            else:
                                print(f"I am sorry, {name}. You failed.")
                                print("Summary of grades: ")
                                print(f"Math: {math}")
                                print(f"English: {eng}")
                                print(f"Science: {sci}")
                                print(f"Languages: {lang}")
                                print(f"Programming: {prog}")
                                print(f"Average: {rounded_average}")
                                print("You got a F.")
                        else:
                            print("Invalid programming grade. Grade must be between 1 and 100.")
                    else:
                        print("Invalid language grade. Grade must be between 1 and 100.")
                else:
                    print("Invalid science grade. Grade must be between 1 and 100.")
            else:
                print("Invalid math grade. Grade must be between 1 and 100.")
        else:
            print("Invalid english grade. Grade must be between 1 and 100.")
    else:
        print("Invalid year level. Year level must be between 1 and 4")
else:
    print("Invalid age. ")