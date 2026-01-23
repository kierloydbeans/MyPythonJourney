name = input("Enter your name: ")
nameValidation = name.isalpha()
if nameValidation == True:
    age = int(input("Enter your age: "))
    if age >= 0 and age <= 120:
        year = int(input(("Enter your year level: ")))
        if year >= 1 and year <= 4:
            print("Enter your grades: ")
            math = int(input("Enter your math grade: "))
            if math >= 0 and math <= 100:
                eng = int(input("Enter your english grade: "))
                if eng >= 0 and eng <= 100:
                    prog = int(input("Enter you programming grade:"))
                    if prog >= 0 and prog <= 100:
                        average = ((math + eng + prog) / 3)
                        rounded_average = round(average, 2)
                        print(f"Hello {name}")
                        print("Summary of grades: ")
                        print(f"Math : {math}")
                        print(f"English : {eng}")
                        print(f"Programming : {prog}")
                        print(f"Rounded Average : {rounded_average}")
                        if rounded_average >= 75:
                            print("You passed!")
                            if rounded_average >= 96 and rounded_average <= 100:
                                print("You got A.")
                            elif rounded_average >= 91 and rounded_average <= 95:
                                print("You got B.")
                            elif rounded_average >= 86 and rounded_average <= 90:
                                print("You got C.")
                            elif rounded_average >= 81 and rounded_average <= 85:
                                print("You got D.")
                            elif rounded_average >= 76 and rounded_average <= 80:
                                print("You got E.")
                        else:
                            print("You failed.")
                            print("You got F.")
                    else:
                        print("Invalid programming grade. Grade must be between 0 and 100")
                else:
                    print("Invalid english grade. Grade must be between 0 and 100")
            else:
                print("Invalid math grade. Grade must be between 0 and 100")
        else:
            print("Invalid year level. It should be between 1 and 4")
    else:
        print("Invalid age. Age should be between 0 and 120")
else:
    print("Invalid. We only accept alphabet characters.")