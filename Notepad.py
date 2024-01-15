from tkinter import *
from tkinter import filedialog

# Create the main window
window = Tk()
window.title("Simple Notepad")
window.geometry("600x600")
window.config(bg='blue')  # Set background color
window.resizable(False, False)

# Function to save the entered text to a file
def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')  
    # This function prompts the user to select a file location and name for saving.
    if open_file is None:
        return  # If the user cancels the operation, return without saving.
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

# Function to open a text file and display its content
def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    # This function prompts the user to select a file to open.
    if file is not None:
        content = file.read()
        entry.insert(INSERT, content)  # Insert the content into the Text widget named entry.

# Buttons for Save and Open operations
save = Button(window, width='20', height='2', bg='#fff', text='Save file', command=save_file).place(x=100, y=5)
open_btn = Button(window, width='20', height='2', bg='#fff', text='Open file', command=open_file).place(x=300, y=5)

# Text entry field
entry = Text(window, height='33', width='72')
entry.place(x=10, y=60)

# Start the Tkinter event loop
window.mainloop()