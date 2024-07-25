

# Custom Functions
# This Function gives us the get_todos in read mode.
def get_todos(filepath="Experiment1File.txt"):
    """ Read a txt file and then returns the list
    of to-do items."""
    with open(filepath, "r") as file:
        todo_items = file.readlines()
    return todo_items


# Custom Functions
# This Function gives us the get_todos and writes the information into the file.
def write_todos(todo_items):
    """ Writes the to-do items list on the txt file. """

    with open("../2. Defining Functions/Experiment1File.txt", "w") as file:
        file.writelines(todo_items)


# Start an infinite loop to continuously prompt the user for actions
while True:
    user_action = input("Type add, show, edit, completed, delete, clear or exit: ")
    user_action = user_action.strip().lower()

    # Check if the user action is one of the recognized commands
    if user_action in ["add", "show", "edit", "completed", "delete", "clear"]:
        # Use the get_todos function to read the todo list from the file
        todos = get_todos("../2. Defining Functions/Experiment1File.txt")

        if user_action == "add":
            # Prompt the user to enter a new todo item
            todo = input("Enter the todo item: ").strip()
            # Add the new todo item to the list
            todos.append(todo + "\n")
            # Write the updated todo list back to the file
            write_todos(todos)

        elif user_action == "show":
            # Display all todo items with their index in a formatted manner
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item.capitalize()}"
                print(row)

        elif user_action == "edit":
            try:
                # Prompt the user to enter the number of the todo item to edit
                number = int(input("Number of the todo to edit: ")) - 1

                # Check if the number is within the valid range
                if 0 <= number < len(todos):
                    # Prompt the user to enter the new todo item
                    new_todo = input("Enter new todo: ").strip()
                    # Update the specified todo item
                    todos[number] = new_todo + "\n"
                    # Write the updated todo list back to the file
                    write_todos(todos)
                else:
                    print("Invalid number! Please try again.")
            except ValueError:
                # Handle invalid input for the number
                print("Please enter a valid number.")

        elif user_action == "completed":
            try:
                # Prompt the user to enter the number of the todo item to mark as completed
                number = int(input("Number of the todo to complete: ")) - 1

                # Check if the number is within the valid range
                if 0 <= number < len(todos):
                    # Remove the specified todo item and strip the newline character
                    todo_to_remove = todos.pop(number).strip("\n")
                    # Write the updated todo list back to the file
                    write_todos(todos)
                    # Inform the user that the todo item was removed
                    message = f"Todo '{todo_to_remove}' was removed from the list!"
                    print(message)
                else:
                    print("Invalid number! Please try again.")
            except ValueError:
                # Handle invalid input for the number
                print("Please enter a valid number.")

        elif user_action == "delete":
            # Prompt the user to enter the numbers of the todo items to delete, separated by commas
            numbers_str = input("Numbers of the todos to delete (comma-separated): ").strip()
            # Convert the input string into a list of integers, adjusting for zero-based indexing
            numbers = [int(num.strip()) - 1 for num in numbers_str.split(',') if num.strip().isdigit()]
            # Sort the numbers in reverse order to avoid index shifting issues
            numbers.sort(reverse=True)

            # Delete each specified todo item, checking for valid indices
            for number in numbers:
                if 0 <= number < len(todos):
                    del todos[number]
                else:
                    print(f"Invalid todo number {number + 1}. Skipping...")

            # Write the updated todo list back to the file
            write_todos(todos)

        elif user_action == "clear":
            # Clear the todo list
            todos.clear()
            # Write the empty todo list back to the file
            write_todos(todos)

    elif user_action == "exit":
        # Exit the loop and end the program
        break

    else:
        # Inform the user of an invalid command
        print("Your command is not valid! Please enter the right command!")

# Print a goodbye message when the loop ends
print("Bye!!!!")
