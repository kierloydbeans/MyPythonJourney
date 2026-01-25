# name, age, five grades, average, summary, pass or fail, failed subjects. all with validation

name = input("Enter your name: ")
nameValidation = name.isalpha()
if nameValidation == True:
    ageInput = input("Enter your age: ")
    ageInputValidation = ageInput.isdigit()
    if ageInputValidation == True:
        age = int(ageInput)
        if age >= 0 and age <= 120:
            yearLevelInput = input("Enter your year level: ")
            yearLevelInputValidation = yearLevelInput.isdigit()
            if yearLevelInputValidation == True:
                yearLevel = int(yearLevelInput)
                if yearLevel >= 1 and yearLevel <= 4:
                    mathInput = input("Enter your math grades: ")
                    mathInputValidation = mathInput.isdigit()
                    if mathInputValidation == True:
                        math = int(mathInput)
                        if math >= 0 and math <= 100:
                            englishInput = input("Enter your english grades: ")
                            englishInputValidation = englishInput.isdigit()
                            if englishInputValidation == True:
                                english = int(englishInput)
                                if english >= 0 and english <= 100:
                                    sciInput = input("Enter your science grade: ")
                                    sciInputValidation = sciInput.isdigit()
                                    if sciInputValidation == True:
                                        sci = int(sciInput)
                                        if sci >= 0 and sci <= 100:
                                            progInput = input("Enter your programming grade: ")
                                            progInputValidation = progInput.isdigit()
                                            if progInputValidation == True:
                                                prog = int(progInput)
                                                if prog >= 0 and prog <= 100:
                                                    dbInput = input("Enter you database grade: ")
                                                    dbInputValidation = dbInput.isdigit()
                                                    if dbInputValidation == True:
                                                        db = int(dbInput)
                                                        if db >= 0 and db <= 100:
                                                            average = ((math + sci + english + prog + db) / 5)
                                                            roundedAverage = round(average, 2)
                                                            print(f"Welcome {name} of Year {yearLevel}, aged {age}.")
                                                            print("Summary: ")
                                                            print(f"Math {math}")
                                                            print(f"English {english}")
                                                            print(f"Science: {sci}")
                                                            print(f"Programming: {prog}")
                                                            print(f"Database: {db}")
                                                            print(f"Your average is {roundedAverage}")
                                                            if roundedAverage >= 75 and math >= 75 and sci >= 75 and english >= 75 and prog >= 75 and db >= 75:
                                                                print("You passed!")
                                                                if roundedAverage >= 95 and roundedAverage <= 100:
                                                                    print("You got A.")
                                                                elif roundedAverage >= 90 and roundedAverage <= 94:
                                                                    print("You got B.")
                                                                elif roundedAverage >= 85 and roundedAverage <= 89:
                                                                    print("You got C.")
                                                                elif roundedAverage >= 80 and roundedAverage <= 84:
                                                                    print("You got D.")
                                                                elif roundedAverage >= 75 and roundedAverage <= 79:
                                                                    print("You got E.")
                                                            elif roundedAverage >= 75 and (math < 75 or english < 75 or sci < 75 or prog < 75 or db < 75):
                                                                print("You passed but you have to retake the following subjects: ")
                                                                if math < 75:
                                                                    print(f"- Math. You got {math}")
                                                                if english < 75:
                                                                    print(f"- English. You got {english}")
                                                                if sci < 75:
                                                                    print(f"- Science. You got {sci}")
                                                                if prog < 75:
                                                                    print(f"- Programming. You got {prog}")
                                                                if db < 75:
                                                                    print(f"- Database. You got {db}")
                                                            else:
                                                                print("You failed.")
                                                                print("You got F.")
                                                    else:
                                                        print("Invalid. Input only numbers.")
                                                else:
                                                    print("Grade must be between 0 and 100.")
                                            else:
                                                print("Invalid. Enter only numbers.")
                                        else:
                                            print("Grade must be between 0 and 100.")
                                    else:
                                        print("Invalid. ENter only numbers.")
                                else:
                                    print("Grade must be between 0 and 100.")
                            else:
                                print("Invalid. Enter only numbers.")
                        else:
                            print("Grade must be between 0 and 100")
                    else:
                        print("Invalid. Enter only numbers.")
                else:
                    print("Year level must be within 1 and 4")
            else:
                print("Invalid. Enter only numbers.")
        else:
            print("Invalid. Age should be between 0 and 120.")
    else:
        print("Invalid. Enter only numbers")
else:
    print("Invalid. Enter only alphabet characters.")

# time spent: 39:41.89