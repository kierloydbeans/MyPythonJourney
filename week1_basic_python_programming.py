name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age > 0 and age < 150 :  # age validation
    year = int(input("Enter your year level: "))
    if year < 5 and year > 0:  # year level validation
        print("Please enter your grades ")
        math = int(input("Math: "))
        if math <= 100:  # math validation
            english = int(input("English: "))
            if english <= 100:  # english validation
                sci = int(input("Science: "))
                if sci <= 100:  # science validation
                    prog = int(input("Programming: "))
                    if prog <= 100:  # programming validation
                            print(f"The summary of your grades is: \nMath: {math} \nEnglish: {english} \nScience: {sci} \nProgramming: {prog}")
                            average = ((math + english + sci + prog) / 4)  # compute average
                            rounded_average = round(average, 2)  # round average to 2 decimal points
                            print(f"Your final grade is {rounded_average}.")
                            if average <= 100 and average >= 98:  # conversion to college grading system
                                print("You got 1.00")
                            elif average <= 97 and average >= 95:
                                print("You got 1.25")
                            elif average <= 94 and average >= 92:
                                print("You got 1.50")
                            elif average <= 91 and average >= 89:
                                print("You got 1.75")
                            elif average <= 88 and average >= 86:
                                print("You got 2.00")
                            elif average <= 85 and average >= 83:
                                print("You got 2.25")
                            elif average <= 82 and average >= 80:
                                print("You got 2.50")
                            elif average <= 79 and average >= 77:
                                print("You got 2.75")
                            elif average <= 76 and average >= 75:
                                print("You got 3.00")
                            elif average < 75:
                                print("Sorry, you got 5.00")
                    else:
                        print("Invalid programming grade.")
                else:
                    print("Invalid science grade.")
            else:
                print("Invalid english grade.")
        else:
            print("Invalid math grade.")
    else:
        print("Invalid input. Please put a valid year level.")
else:
    print("Invalid input. Input a valid age.")