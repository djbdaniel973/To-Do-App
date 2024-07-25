

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


if __name__ == "__main__":
    print("hello from functions!!!!")
    print(get_todos())
