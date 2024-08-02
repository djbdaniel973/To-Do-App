import functions
import FreeSimpleGUI as sg

def add_todo():
    todos = functions.get_todos()
    new_todo = values["todo"].strip() + "\n"
    if new_todo.strip():  # Ensure new_todo is not empty
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

def delete_todo():
    if values["todos"]:  # Ensure there's a selected item
        todo_to_delete = values["todos"][0]
        todos = functions.get_todos()
        if todo_to_delete in todos:
            todos.remove(todo_to_delete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")
        else:
            sg.popup("Error", "Selected todo not found.")
    else:
        sg.popup("Error", "Please select a todo item to delete.")

# Define UI components
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 15])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Completed")
delete_button = sg.Button("Delete")  # Added Delete button
clear_button = sg.Button("Clear")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box], [edit_button],
                           [complete_button], [delete_button], [clear_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    if "todos" in values and values["todos"]:  # Ensure "todos" key exists and is not empty
        print(3, values["todos"])

    if event == "Add":  # Handle adding todo
        if values["todo"]:  # Check if input box is not empty
            add_todo()

    elif event == "Edit":
        if values["todos"]:  # Check if there's a selected item
            todo_to_edit = values["todos"][0]  # Get the selected item
            new_todo = values["todo"].strip() + "\n"

            todos = functions.get_todos()
            if todo_to_edit in todos:
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            else:
                sg.popup("Error", "Selected todo not found.")
        else:
            sg.popup("Error", "Please select a todo item to edit.")

    elif event == "Completed":
        if values["todos"]:  # Ensure there's a selected item
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")

    elif event == "Delete":
        delete_todo()  # Handle deleting todo

    elif event == "Clear":
        todos = functions.get_todos()  # Fetch the current todos
        todos.clear()  # Clear the todo list
        functions.write_todos(todos)  # Write the empty list back to the file
        window["todos"].update(values=todos)  # Update the listbox
        window["todo"].update("")  # Clear the input box

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
