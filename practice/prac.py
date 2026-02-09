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

# num = int(input("Enter a number: "))
# limit = int(input("Enter a limit: "))
#
# finalNum = 1
# currentNum = 1
#
# for currentNum in range(1, limit+1):
#     finalNum = num * currentNum
#     currentNum += 1
#     print(finalNum)

start = int(input("Enter a number: "))
end = int(input("Enter ending number: "))

finalNum = 0
currentNum = start

while currentNum <= end:
    if currentNum % 2 == 0:
        finalNum = finalNum + currentNum
        print(f"{finalNum} is even")
    else:
        finalNum = finalNum + currentNum
        print(f"{finalNum} is odd")
    currentNum = currentNum + 1

print(f"The total number is: {finalNum}")