import functions
import FreeSimpleGUI as sg
# sg REPRESENTS FreeSimpleGUI. Is shorter and easier to write and access.

label1 = sg.Text("Type in a to-do")
input_box1 = sg.InputText(tooltip="Enter todo", key = "todo")
add_button1 = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label1], [input_box1], [add_button1]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break



window.close()


