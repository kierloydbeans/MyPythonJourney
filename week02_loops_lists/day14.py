# to do list
# add to do
# remove to do
# view to do
# exit

# logic done in 00:14:52.630
# with validation done in 00:30:50.026
todo = {}

while True:
    print("-"*30)
    print("To Do List")
    print("-" * 30)
    print("1. Add a task\n")
    print("2. Remove a task\n")
    print("3. View all tasks\n")
    print("5. Exit\n")

    choice = input("Enter your choice: ")
    if choice.isdigit():
        if choice == "1":
            task = input("Enter a task: ")
            if not task:
                print("\nCan't input a blank task\n")
                continue
            dateTargeted = input("Enter a targeted date for the task completion: ")
            if not dateTargeted:
                print("\nCan't input a blank date\n")
                continue
            todo[task] = dateTargeted
            print("\nData saved. Thank you!\n")
        elif choice == "2":
            if not todo:
                print("\nCan't perform operation. There are no tasks to remove.\n")
                continue
            task = input("Enter the task you want to remove: ")
            if not task in todo:
                print("\nCan't perform operation. Task does not exist.\n")
                continue
            else:
                todo.pop(task)
            print("\nData removed. Thank you!\n")
        elif choice == "3":
            if not todo:
                print("\nCan't perform operation. There are no tasks to display.\n")
            for x in todo:
                print(f"Task: {x} | Targeted Date of Completion: {todo[x]}")
        elif choice == "5":
            print("Exiting...")
            print("Thank you!\n")
            break
        else:
            print("Invalid choice")
    else:
        print("\nInvalid choice. Numbers only\n")