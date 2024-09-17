import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get the expression from the entry widget
        expression = entry.get()
        # Evaluate the expression and display the result
        result = eval(expression)
        result_var.set(f"Result: {result}")
    except Exception as e:
        # Show an error message in case of invalid input
        messagebox.showerror("Error", f"Invalid input: {e}")

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, current_text + value)  # Append the clicked button's value

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar for displaying results
result_var = tk.StringVar()
result_var.set("Result: ")

# Create and place the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 18), bd=10,justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create and place the result label
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 14))
result_label.grid(row=1, column=0, columnspan=4)

# Define the button layout
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky='nsew')

# Adjust grid weights to make buttons resize with window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the GUI event loop
root.mainloop()
