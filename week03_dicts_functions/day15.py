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

days_of_months = {
    "january": "31",
    "february": "28",
    "march": "31",
    "april": "30",
    "may": "31",
    "june": "30",
    "july": "31",
    "august": "31",
    "september": "30",
    "october": "31",
    "november": "30",
    "december": "31"
}

user_session = {
    # "kier":{  username
    #     "March":{  month_now
    #         "1":{  logged day
    #             "time in": "8:00",
    #             "time out": "17:00"
    #         }
    #     }
    # }
}

def login():
    while True:
        username = input("Please enter your username: ")
        if username in users:
            while True:
                password = input("Please enter your password: ")
                if password == users[username]["password"]:
                    mainMenu(username)
                    return username
                else:
                    print("Password incorrect.")
        else:
            print("Username not found.")

def starting():
    while True:
        print(f"Welcome!")
        print("1. Login")
        print("2. Exit\n")
        action = input("Please enter your action: ")
        if action == "1":
            login()
        elif action == "2":
            exit()
        else:
            print("Invalid\n")

def mainMenu(username):
    # create user container
    if username not in user_session:
        user_session[username] = {}
    while True:
        print(f"\nWelcome, {username}!\n")
        print("1. Time in")
        print("2. Time out")
        print("3. Display your time in and out")
        print("4. Calculate accumulated salary")
        print("5. Logout\n")

        month_now = datetime.now().strftime("%B")  # gets current month
        day = str(datetime.now().day)  # gets current day
        now_time = datetime.now().strftime("%H:%M")  # gets current time

        if month_now not in user_session[username]:  # creates month container
            user_session[username][month_now] = {}
        if day not in user_session[username][month_now]:  # creates day container
            user_session[username][month_now][day] = {"time in": None, "time out": None}

        action = input("Please enter your action: ")
        if action == "1":
            user_session[username][month_now][day]["time in"] = now_time
            print("Time in: ", {month_now}, {day}, {now_time})
        elif action == "2":
            user_session[username][month_now][day]["time out"] = now_time
            print("Time out: ", {month_now}, {day}, {now_time})
        elif action == "3":
            print(f"Logs for {month_now}")
            for logged_day, times in user_session[username][month_now].items():
                t_in = times["time in"] if times["time in"] else "N/A"
                t_out = times["time out"] if times["time out"] else "N/A"
                print(f"{logged_day}. Time in: {t_in}, Time out: {t_out}")
        elif action == "5":
            return
        else:
            print("Invalid.\n")
starting()