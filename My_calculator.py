import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showinfo("sometimes when i close this box the math machine closes so yah")

def calculate():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    operation = operation_var.get()
    if operation == 'Add':
        result = number1 + number2
    elif operation == 'Subtract':
        result = number1 - number2
    elif operation == 'Multiply':
        result = number1 * number2
    elif operation == 'Divide':
        result = number1 / number2
    else:
        result = ''
    result_label.config(text=f"Result: {result}")

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result_label.config(text='Result:')

root = tk.Tk()
root.title("math machine")
tk.Label(root, text="math1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="math2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text="wha ya wanna do:").grid(row=2, column=0, padx=5, pady=5)
operation_var = tk.StringVar()
operation_var.set('Add')
tk.Radiobutton(root, text='Add', variable=operation_var, value='Add').grid(row=2, column=1)
tk.Radiobutton(root, text='Subtract', variable=operation_var, value='Subtract').grid(row=2, column=2)
tk.Radiobutton(root, text='Multiply', variable=operation_var, value='Multiply').grid(row=3, column=1)
tk.Radiobutton(root, text='Divide', variable=operation_var, value='Divide').grid(row=3, column=2)
tk.Button(root, text='Calculate', command=calculate).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text='Clear', command=clear).grid(row=4, column=1, padx=5, pady=5)
result_label = tk.Label(root, text='Result:')
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()
