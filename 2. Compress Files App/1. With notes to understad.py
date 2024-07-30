
# Notes step by ste:

# 1. This first line imports the FreeSimpleGUI Phython Library.
import FreeSimpleGUI as sg

# """ FreeSimpleGUI is a Python library that makes it easy to create Graphical User Interfaces (GUIs).
# It aims to simplify the process of designing and implementing user interfaces,
# making it accessible even for those who may not have extensive experience with GUI development."""



label1 = sg.Text("Select file to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button]])

window.read()
window.close()