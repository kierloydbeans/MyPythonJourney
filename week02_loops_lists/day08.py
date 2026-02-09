# ## ✅ Task 1 – Simple Loop Warm-up (5–10 mins)
#
# **Objective:** Understand what a loop *feels* like.
#
# Create a program that:
#
# * Asks for a number
# * Keeps asking **until the user inputs a valid integer between 1 and 10**
# * Prints:
#   `Thank you! You entered X`
#
# 👉 Rules:
#
# * Use `while`
# * Use `.isdigit()`
# * No `break` yet (discipline 😈)

numInput = input("Enter a number: ")
# if not
while not numInput.isdigit():
    print("Invalid Input. Numbers only.")
    numInput = input("Enter a number: ")
# if yes
num = int(numInput)
while num <= 0 or num > 10:
    print("Invalid Input. Number must be between 1 and 10.")
    numInput = input("Enter a number: ")
    while not numInput.isdigit():
        print("Invalid Input. Numbers only.")
        numInput = input("Enter a number: ")
    num = int(numInput)
print(f"Number accepted: {num}")

#time spent: 09:04.21

# ## ✅ Task 2 – Age Validation (Your Old Enemy, But Easier Now)
#
# Rewrite **ONLY the age input part** from your previous programs using a loop.
#
# Behavior:
#
# * Ask for age
# * If:
#
#   * not numeric → show friendly error
#   * out of range (0–120) → explain why
# * Keep asking **until valid**
# * Then print:
#   `Age accepted: X`
#
# 💡 This should already feel **less painful** than Day 6.
#
# ---

ageInput = input("Enter your age: ")
while not ageInput.isdigit():
    print("Invalid Age. Must be a number.")
    ageInput = input("Enter your age: ")
age = int(ageInput)
while age < 0 or age >= 120:
    print("Invalid Age. Must be between 1 and 120.")
    ageInput = input("Enter your age: ")
    while not ageInput.isdigit():
        print("Invalid Age. Must be a number.")
        ageInput = input("Enter your age: ")
    age = int(ageInput)
print(f"Accepted: {age}")

# time spent: time not recorded; timer crashed

# ## ✅ Task 3 – Grade Input With Retry (ONE SUBJECT ONLY)
#
# Choose **Math**.
#
# Requirements:
#
# * Ask for math grade
# * Validate:
#
#   * numeric
#   * 0–100
# * If invalid:
#
#   * explain the mistake
#   * retry
# * Once valid:
#
#   * print `Math grade recorded: X`
#
# 🚫 Do NOT add other subjects yet.
#
# ---

mathInput = input("Enter math grade: ")
while not mathInput.isdigit():
    print("Invalid math grade. Only numbers are accepted.")
    mathInput = input("Enter math grade: ")
math = int(mathInput)
while math < 0 or math > 100:
    print("Invalid grade. Must be between 0 and 100.")
    mathInput = input("Enter math grade: ")
    while not mathInput.isdigit():
        print("Invalid grade. Only numbers.")
        mathInput = input("Enter math grade: ")
    math = int(mathInput)
print(f"Accepted: Grade is {math}.")

# time spent : 06:46.60