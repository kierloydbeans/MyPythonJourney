# ask for name, age, year level, 3 grades, compute average, rounded average, letter equivalent, display complete summary with failed subjects

name = input("Enter your name: ")
nameValidation = name.isalpha()
if nameValidation == True:
    age = input("Enter your age: ")
    ageValidation = age.isdigit()
    if ageValidation == True:
        age = int(age)
        if age >= 0 and age <= 120:
            year = input("Enter your year level: ")
            yearValidation = year.isdigit()
            if yearValidation == True:
                year = int(year)
                if year >= 1 and year <= 4:
                    print(f"Welcome {name}!")
                    print("------------------------------")
                    math = input("Enter your grade in math: ")
                    mathValidation = math.isdigit()
                    if mathValidation == True:
                        math = int(math)
                        if math >= 0 and math <= 100:
                            science = input("Enter you science grade: ")
                            scienceValidation = science.isdigit()
                            if scienceValidation == True:
                                science = int(science)
                                if science >= 0 and science <= 100:
                                    programming = input("Enter your programming grade: ")
                                    programmingValidation = programming.isdigit()
                                    if programmingValidation == True:
                                        programming = int(programming)
                                        if programming >= 0 and programming <= 100:
                                            print("SUMMARY OF GRADES")
                                            print(f"Math: {math}")
                                            print(f"Science: {science}")
                                            print(f"Programming: {programming}")
                                            average = ((math + science + programming) / 3)
                                            rounded_average = round(average, 2)
                                            print(f"Your average grade is {rounded_average}")
                                            if rounded_average >= 75 and math >= 75 and science >= 75 and programming >= 75:
                                                print("Great! You passed all subjects! :D")
                                                if rounded_average >= 95 and rounded_average <= 100:
                                                    print("You got A!")
                                                elif rounded_average >= 90 and rounded_average <= 94:
                                                    print("You got B!")
                                                elif rounded_average >= 85 and rounded_average <= 89:
                                                    print("You got C!")
                                                elif rounded_average >= 80 and rounded_average <= 84:
                                                    print("You got D!")
                                                elif rounded_average >= 75 and rounded_average <= 79:
                                                    print("You got E!")
                                            elif rounded_average >= 75 and (math < 75 or science < 75 or programming < 75):
                                                print("You passed the subjects but have to retake the following: ")
                                                if math < 75:
                                                    print("Math.")
                                                if science < 75:
                                                    print("Science.")
                                                if programming < 75:
                                                    print("Programming.")
                                            else:
                                                print("I'm sorry. You failed. :'(")
                                                if rounded_average <= 74 and rounded_average >= 0:
                                                    print("You got F!")
                                        else:
                                            print("Invalid programming grade. Grade must be between 0 and 100.")
                                    else:
                                        print("Invalid programming grade. Enter only positive numbers.")
                                else:
                                    print("Invalid science grade. Grade must be between 0 and 100.")
                            else:
                                print("Invalid science grade. Enter only positive numbers.")
                        else:
                            print("Invalid math grade. Grade must be between 0 and 100.")
                    else:
                        print("Invalid Grade. Enter only positive numbers.")
                else:
                    print("Invalid year level. It must be between 1 and 4")
            else:
                print("Invalid year level. Enter only positive numbers.")
        else:
            print("Your age must be between 0 and 120")
    else:
        print("Invalid age. Enter only numbers")
else:
    print("Invalid Name. Enter alphabet characters.")