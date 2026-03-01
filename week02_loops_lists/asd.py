# while True:
#     numOneInput = input("Enter first number: ")
#     if not numOneInput.isdigit():
#         print("Must be a number.")
#         continue
#     numTwoInput = input("Enter second number: ")
#     if not numTwoInput.isdigit():
#         print("Must be a number.")
#         continue
#
#     num1 = int(numOneInput)
#     num2 = int(numTwoInput)
#
#     sum = num1 + num2
#     if sum % 2 == 0:
#         print(f"{sum} is Even.")
#     else:
#         print(f"{sum} is Odd.")
#
#     con = input("Do you want to continue? 1 if yes, other char if no: ")
#     if con == "1":
#         continue
#     elif con == "0":
#         print("Thank you")
#     else:
#         print("Invalid.")
#     break






# while True:
#     num1Input = input("Enter first number: ")
#     if not num1Input.isdigit():
#         print("Invalid. Must be a number.")
#         continue
#
#     num2Input = input("Enter second number: ")
#     if not num2Input.isdigit():
#         print("Invalid. Must be a number.")
#         continue
#
#     num1 = int(num1Input)
#     num2 = int(num2Input)
#
#     sum = num1 + num2
#
#     if sum % 2 == 0:
#         print(f"{num1} + {num2} = {sum}. {sum} is Even.")
#     else:
#         print(f"{num1} + {num2} = {sum}. {sum} is Odd.")
#
#     while True:
#         con = input("DO you want to continue? Y if yes, N if no.")
#         if con == "Y":
#             break
#         elif con == "N":
#             print("Thank you!")
#             exit()
#         else:
#             print("Invalid.")

while True:
    num1Input = input("Enter first number: ")
    if not num1Input.isdigit():
        print("Invalid. Must be a number.")
        continue

    num2Input = input("Enter second number: ")
    if not num2Input.isdigit():
        print("Invalid. Must be a number.")
        continue

    num1 = int(num1Input)
    num2 = int(num2Input)

    sum = num1 + num2
    if sum % 2 == 0:
        print(f"{num1} + {num2} = {sum}. {sum} is even.")
    else:
        print(f"{num1} + {num2} = {sum}. {sum} is odd.")

    while True:
        con = input("Do you want to continue? Y/N: ")
        if con == "Y" or con == "y":
            continue
        elif con == "N" or con == "n":
            print("Thank you!")
            exit()
        else:
            print("Invalid")