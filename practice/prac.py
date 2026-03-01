# while True:
#     numInput = input("Enter a number: ")
#     if not numInput.isdigit():
#         print("Please enter a number.")
#         continue
#     num = int(numInput)
#     break
#
# while True:
#     limitInput = input("Enter a limit: ")
#     if not limitInput.isdigit():
#         print("Please enter a number.")
#         continue
#     limit = int(limitInput)
#     break
#
# finalNum = 1
# currentNum = 1
#
# while currentNum <= limit:
#     finalNum = num * currentNum
#
#     if finalNum % 2 == 0:
#         status = "EVEN"
#     else:
#         status = "ODD"
#     print(f"{num} x {currentNum} = {finalNum} ({status})")
#     currentNum = currentNum + 1
# 
# num = int(input("Enter a number: "))
# limit = int(input("Enter a limit: "))
# 
# finalNum = 1
# currentNum = 1
# 
# while currentNum <= limit:
#     finalNum = num * currentNum
# 
#     if finalNum % 2 == 0:
#         status = "EVEN"
#     else:
#         status = "ODD"
# 
#     print(f"{num} x {currentNum} = {finalNum}({status})")
#     currentNum = currentNum + 1
#
# num = int(input("Enter a number: "))
# limit = int(input("Enter a limit: "))
#
# finalNum = 1
# currentNum = 0
#
# for currentNum in range(1, limit+1):
#     finalNum = num + currentNum
#     print(f"{num} + {currentNum} = {finalNum}")
#     currentNum += 1

# username = "user"
# password = "pass"
# contactNum = "09123456789"
# while True:
#     usernameInput = input("Enter username: ")
#     if not usernameInput == username:
#         print("Wrong username")
#         continue
#     break
#
# while True:
#     passwordInput = input("Enter password: ")
#     if not passwordInput == password:
#         print("Wrong password.")
#         continue
#     break
#
# while True:
#     contactNumInput = input("Enter contact number: ")
#     if not contactNumInput.isdigit():
#         print("Invalid. Numbers only.")
#         continue
#     if contactNumInput == contactNum:
#         print("Number already taken.")
#         continue
#     break
#
# print(f"Welcome {username}")