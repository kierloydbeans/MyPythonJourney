# log time in
# log time out
# calculate hours worked
# calculate accumulated salary
# calculate estimated annual salary

from datetime import datetime

users = {
    "kier": {
        "password": "password",
        "position": "junior",
        "salary": "150"
    }
}

def login():
    while True:
        username = input("Please enter your username: ")
        if username in users:
            while True:
                password = input("Please enter your password: ")
                if password == users[username]["password"]:
                    mainMenu()
                    return username
            else:
                print("Password incorrect.")
        else:
            print("Username not found.")
    return None

def starting():
    while True:
        print("Welcome!")
        print("1. Login")
        print("2. Logout")
        action = input("Please enter your action: ")
        if action == "1":
            login()
        elif action == "2":
            exit()

def mainMenu():
    print("Welcome!")
    print("1. Time in")
    print("2. Time out")
    print("3. Calculate accumulated salary")
    action = input("Please enter your action: ")
    if action == "1":
        startTime = datetime.now()
        print("Time taken: ", datetime.now())
starting()