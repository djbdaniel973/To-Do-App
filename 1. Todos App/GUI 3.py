import functions
import FreeSimpleGUI as sg

# sg REPRESENTS FreeSimpleGUI. Is shorter and easier to write and access.

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 15])

edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box], [edit_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    if values["todos"]:  # Check if there are selected items
        print(3, values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].strip() + "\n"
            if new_todo:  # Ensure the new todo is not empty
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)  # Update the listbox
                window["todo"].update("")  # Clear the input box after adding

        case "Edit":
            if values["todos"]:  # Check if there's a selected item
                todo_to_edit = values["todos"][0].strip()  # Get the selected item and strip newline
                new_todo = values["todo"].strip() + "\n"

                todos = functions.get_todos()
                if todo_to_edit in todos:
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window["todos"].update(values=todos)  # Update the listbox
                    window["todo"].update("")  # Clear the input box after editing
                else:
                    sg.popup("Error", "Selected todo not found.")
            else:
                sg.popup("Error", "Please select a todo item to edit.")

        case "todos":
            # You probably want to update the input box with the selected todo
            if values["todos"]:
                window["todo"].update(value=values["todos"][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
