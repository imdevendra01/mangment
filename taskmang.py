# Title of Project: The Management App
# Objective: To create a task management application where users can add, update, delete, view, and manage tasks.

# Since this project does not involve typical data science tasks such as importing data from a source, visualizing, etc., 
# I will demonstrate the core functionalities of the task management application with appropriate comments.

# Import Library
# (For this task management app, we are using only basic Python, so no external libraries are needed.)

# Import Data
# (No external data to import, as tasks will be input by the user during the program's execution.)

# Describe Data
# (The data here refers to the tasks that the user will input, stored in a list.)

# Data Visualization
# (Not applicable in this context, as we are not dealing with data that needs visualization.)

# Data Preprocessing
# (Not applicable, as tasks are simply strings entered by the user.)

# Define Target Variable (y) and Feature Variables (X)
# (Not applicable here; the tasks themselves are the main elements of interest.)

# Train Test Split
# (Not applicable as this is not a machine learning task.)

# Modeling
# (The following code represents the core of the task management functionality.)

def task():
    tasks = []  # Initialize an empty list to store tasks
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    total_task = int(input("Enter how many tasks you want to add = "))
    
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
            
            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")
            
            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                
                if updated_val in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task '{updated_val}' to '{up}'.")
                else:
                    print("Task not found.")
            
            elif operation == 3:
                del_val = input("Which task you want to delete = ")
                
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
            
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            
            elif operation == 5:
                print("Closing the program....")
                break
            
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

# Model Evaluation
# (Not applicable as no model is being evaluated. The user simply interacts with the task management system.)

# Prediction
# (Not applicable as this is not a prediction-based project.)

# Explanation
# This task management app allows users to:
# 1. Add tasks.
# 2. Update existing tasks.
# 3. Delete tasks.
# 4. View the list of tasks.
# 5. Exit the application.

# The tasks are stored in a list and the user can manage them through simple menu-driven operations.

# Running the task management application
task()