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

#input
numInput = input("Enter a number: ")
# if not
while not numInput.isdigit():
    print("Invalid Input. Numbers only")
    numInput = input("Enter a number: ")
# if yes
num = int(numInput)
#validation
#if no
while num < 1 or num > 10:
    print("Invalid Input. Numbers must be between 0 and 10")
    numInput = input("Enter a number: ")
    #if no
    while not numInput.isdigit():
        print("Invalid Input. Numbers only")
        numInput = input("Enter a number: ")
    #if yes
    num = int(numInput)
print(f"Thank you! You entered {num}")

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
#if not
while not ageInput.isdigit():
    print("Invalid Input. Numbers only")
    ageInput = input("Enter your age: ")

#if yes
age = int(ageInput)
while age < 0 or age > 120:
    print("Invalid Input. Age must be between 0 and 120")
    ageInput = input("Enter your age: ")
    while not ageInput.isdigit():
        print("Invalid Input. Numbers only")
        ageInput = input("Enter your age: ")
    age = int(ageInput)
print(f"Age accepted: {age}")

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

mathInput = input("Enter your math grade: ")
#if no
while not mathInput.isdigit():
    print("Invalid Input. Must be a number.")
    mathInput = input("Enter your math grade: ")

#if yes
math = int(mathInput)
while math < 0 or math > 100:
    print("Invalid Input. Must be between 0 and 100.")
    mathInput = input("Enter your math grade: ")
    while not mathInput.isdigit():
        print("Invalid Input. Must be a number.")
        mathInput = input("Enter your math grade: ")
    math = int(mathInput)
print(f"Math grade recorded: {math}")

# ## ✅ Task 4 – Reflection Print (Very Important)
#
# At the end of the program, print:
#
# ```
# Loops allow users to recover from mistakes.
# This is better system design.
# ```
#
# This locks the concept into your brain.

print("\nLoops allow users to recover from mistakes.")
print("This is better system design.")