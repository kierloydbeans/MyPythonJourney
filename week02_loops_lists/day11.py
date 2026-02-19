while True:
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Invalid. Letters only.")
        continue
    break

while True:
    ageInput = input("Enter your age: ")
    if not ageInput.isdigit():
        print("Invalid. Numbers only")
        continue

    age = int(ageInput)
    if age < 0 or age >= 120:
        print("Invalid. Must be 0 - 120")
    print("Age valid.")
    break

while True:
    secInput = input("Enter security level: ")
    if not secInput.isdigit():
        print("Invalid. Numbers only.")
        continue

    sec = int(secInput)
    if sec > 5 or sec < 0:
        print("Out of range (1-5)")
        continue
    print(f"Accepted. Your security level is {sec}.")
    if sec == 5:
        print("High security.")
    elif sec >= 3 and sec <= 4:
        print("Moderate security.")
    elif sec >= 1 and sec <= 2:
        print("Low security.")
    break