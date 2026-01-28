# name
nameInput = input("Enter name: ")
while not nameInput.isalpha():
    print("Invalid input. Letters only.")
    nameInput = input("Enter valid name: ")
# age
ageInput = input("Enter age: ")
while not ageInput.isdigit():
    print("Invalid input. Numbers only.")
    ageInput = input("Enter a valid age: ")
age = int(ageInput)
while age < 0 or age >= 120:
    print("Invalid age. Must be between 0 and 100.")
    ageInput = input("Enter a valid age: ")
    while not ageInput.isdigit():
        print("Invalid input. Must be a number.")
        ageInput = input("Enter your valid age: ")
    age = int(ageInput)
# math
mathInput = input("Enter you math grade: ")
while not mathInput.isdigit():
    print("Invalid math grade. Numbers only.")
    mathInput = input("Enter a valid math grade: ")
math = int(mathInput)
while math < 0 or math > 100:
    print("Invalid math grade. Must be between 0 and 100.")
    mathInput = input("Enter a valid grade: ")
    while not mathInput.isdigit():
        print("Invalid math grade. Must be a number.")
        mathInput = input("Enter a valid math grade: ")
    math = int(mathInput)
# english
englishInput = input("Enter you english grade: ")
while not englishInput.isdigit():
    print("Invalid english grade. Numbers only.")
    englishInput = input("Enter a valid english grade: ")
english = int(englishInput)
while english < 0 or english > 100:
    print("Invalid english grade. Must be between 0 and 100.")
    englishInput = input("Enter a valid grade: ")
    while not englishInput.isdigit():
        print("Invalid english grade. Must be a number.")
        englishInput = input("Enter a valid english grade: ")
    english = int(englishInput)
# programming
progInput = input("Enter your programming grade: ")
while not progInput.isdigit():
    print("Invalid programming grade. Must be a number.")
    progInput = input("Enter a valid programming grade: ")
prog = int(progInput)
while prog < 0 or prog > 100:
    print("Invalid programming grade: ")
    progInput = input("Enter a valid programming grade: ")
    while not progInput.isdigit():
        print("Invalid programming grade. Must be a number.")
        progInput = input("Enter a valid programmming grade: ")
    prog = int(progInput)
# average and summary
average = ((math + english + prog) / 3)
roundedAverage = round(average, 2)
print(f"Summary of grades: \nMath: {math} \nEnglish: {english} \nProgramming: {prog} \nAverage: {roundedAverage}")

# time spent: 22:58.61