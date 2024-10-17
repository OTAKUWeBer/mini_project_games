import subprocess
import os

class TaskList:
    def __init__(self):
        self.tasks_list = []

    @staticmethod
    def clear_screen():
        """Clears the terminal screen depending on the operating system."""
        if os.name == 'nt':  # For Windows
            subprocess.run(['cls'], shell=True)
        else:  # For Unix/Linux/Mac
            subprocess.run(['clear'])

    def add(self, task):
        """Adds a task to the list, ensuring it is not duplicated."""
        if task.lower() not in (t.lower() for t in self.tasks_list):
            self.tasks_list.append(task)
            print(f"'{task}' added to the list.")
        else:
            print(f"'{task}' is already in the list.")

    def display_list(self):
        """Displays all the tasks in the list."""
        if not self.tasks_list:
            print("Your list is empty.")
        else:
            print("________________________")
            print("Your task list:")
            for index, task in enumerate(self.tasks_list, start=1):
                print(f"{index}. {task}")
            print("________________________")

    def check(self, task):
        """Checks if a task is in the list."""
        if task.lower() in (t.lower() for t in self.tasks_list):
            print(f"Yes, '{task}' is on the list.")
        else:
            print(f"No, '{task}' is not on the list.")

    def remove(self, task):
        """Removes a task from the list."""
        for t in self.tasks_list:
            if t.lower() == task.lower():
                self.tasks_list.remove(t)
                print(f"'{task}' has been removed.")
                return
        print(f"'{task}' is not on the list.")

    def run(self):
        """Runs the task list application, prompting user for input."""
        while True:
            self.clear_screen()
            print("\n1. Add a task\n2. Display your list\n3. Check if a task is on the list\n4. Remove a task\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.clear_screen()
                task_name = input("Enter the task: ")
                self.add(task_name)
            elif choice == "2":
                self.clear_screen()
                self.display_list()
            elif choice == "3":
                self.clear_screen()
                task_to_check = input("Enter the task to check: ")
                self.check(task_to_check)
            elif choice == "4":
                self.clear_screen()
                task_to_remove = input("Enter the task to remove: ")
                self.remove(task_to_remove)
            elif choice == "5":
                self.clear_screen()
                confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
                if confirm_exit == 'y':
                    print("Exiting...")
                    break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
            input("\nPress Enter to continue...")

# Instantiate the TaskList class and run the app
if __name__ == "__main__":
    task_manager = TaskList()
    task_manager.run()
