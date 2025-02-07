import os
import time

# Login System
USERNAME = "safdarn295"
PASSWORD = "SAFdar786$$"

def login():
    print("=== Welcome to Safdar's Software ===")
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login Successful!")
        return True
    else:
        print("Incorrect Username or Password! Try Again.")
        return False

# Main Menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Daily Schedule Reminder")
        print("2. File & Data Storage")
        print("3. Finance Tracker")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            daily_schedule()
        elif choice == "2":
            file_storage()
        elif choice == "3":
            finance_tracker()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Feature 1: Daily Schedule Reminder
def daily_schedule():
    schedule = {}
    print("Add your daily schedule (Type 'done' to finish):")

    while True:
        time_input = input("Enter Time (HH:MM): ")
        if time_input.lower() == "done":
            break
        task = input("Enter Task: ")
        schedule[time_input] = task

    print("Your Schedule:")
    for time, task in schedule.items():
        print(f"{time} - {task}")

# Feature 2: File & Data Storage
def file_storage():
    print("File Storage System")
    filename = input("Enter filename to save data: ")
    data = input("Enter data to save: ")

    with open(filename, "w") as file:
        file.write(data)

    print(f"Data saved in {filename}")

# Feature 3: Finance Tracker
def finance_tracker():
    balance = float(input("Enter your current balance: "))
    expenses = float(input("Enter total expenses: "))
    savings = balance - expenses
    print(f"Remaining Balance: {savings}")

# Running the software
if __name__ == "__main__":
    if login():
        main_menu()
