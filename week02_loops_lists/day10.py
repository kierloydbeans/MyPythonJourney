while True:
    name = input("Enter name: ")
    if not name.isalpha():
        print("Invalid input. Only letters.")
        continue
    break

while True:
    ageInput = input("Enter age: ")
    if not ageInput.isdigit():
        print("Invalid input. Only digits.")
        continue
    age = int(ageInput)
    if age <= 0 or age >= 100:
        print("Invalid. Must be between 0 and 100")
        continue
    print(f"Hello {name}! You are accepted with the age of {age}.")
    break

while True:
    mathInput = input("Enter math grade: ")
    if not mathInput.isdigit():
        print("Invalid input. Only numbers.")
        continue
    math = int(mathInput)
    if 0 < math > 100:
        print("Invalid. Must be between 0 and 100.")
        continue
    break

while True:
    engInput = input("Enter english grade: ")
    if not engInput.isdigit():
        print("Invalid input. Only numbers.")
        continue
    eng = int(engInput)
    if 0 < eng > 100:
        print("Invalid. Must be between 0 and 100.")
        continue
    break

while True:
    progInput = input("Enter programming grade: ")
    if not progInput.isdigit():
        print("Invalid input. Only numbers.")
        continue
    prog = int(progInput)
    if 0 < prog > 100:
        print("Invalid. Must be between 0 and 100.")
        continue
    break

roundedAverage = round((math + eng + prog) / 3)

if roundedAverage >= 75:
    print(f"Congrats! You passed with {roundedAverage}")

    if 95 <= roundedAverage <= 100:
        print("You got A")
    elif 90 <= roundedAverage <= 94:
        print("You got B.")
    elif 85 <= roundedAverage <= 89:
        print("You got C.")
    elif 80 <= roundedAverage <= 84:
        print("You got D.")
    elif 75 <= roundedAverage <= 79:
        print("You got E.")
else:
    print(f"You failed with {roundedAverage}.\nYou got F.")