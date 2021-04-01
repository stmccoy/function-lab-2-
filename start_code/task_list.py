tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# 1. Print a list of uncompleted tasks
# 2. Print a list of completed tasks

def print_status(task_list, complete):

    uncompleted_tasks = []

    for task in task_list:
        if task["completed"] == complete:
            uncompleted_tasks.append(task)
    
    return uncompleted_tasks

print(print_status(tasks, True))

# 3. Print a list of all task descriptions

def print_t_description(task_list):
    d_list = []
    for task in task_list:
        d_list.append(task["description"])
    return d_list

print(print_t_description(tasks))

# 4. Print a list of tasks where time_taken is at least a given time

def print_t_task(task_list, time):
    time_list = []

    for task in task_list:
        if task["time_taken"] >= time:
            time_list.append(task)
        
    return time_list

print(print_t_task(tasks, 15))

# 5. Print any task with a given description

def print_task_list_d(task_list, description):
    for task in task_list:
        if task["description"] == description:
            return task
    return "no task found"

print(print_task_list_d(tasks, "Wash Dishes"))

# 6. Given a description update that task to mark it as complete.

def mark_as_completed(task_list, description):
    for task in task_list:
        if task["description"] == description:
            task["completed"] = True
            print(task_list)
            return "task updated"

    return "task not found"

updated_list = mark_as_completed(tasks, "Wash Dishes")
print(updated_list)


# 7. Add a task to the list

def add_task(task_list, added_task):
    task_list.append(added_task)

new_task = {"description": "Car Wash", "completed": False, "time_taken": 12}

add_task(tasks, new_task)
print(tasks)

# 8. Use a while loop to display the following menu and allow the use to enter an option.

# ```python


def display_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

display_menu()

while True:
    user_choice = str.lower(input("Please choose an option\n"))

    if user_choice == "q":
       break 
    elif user_choice == "m":
        display_menu()


