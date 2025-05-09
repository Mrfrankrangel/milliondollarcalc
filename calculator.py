# 5/05/2025

import tkinter as tk

root = tk.Tk()
root.title("Million Dollar Calculator")
root.geometry("322x421")
root.resizable(False, False)
root.configure(bg="#ff9900")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()

entry = tk.Entry(
    root, textvariable=equation, font=('Arial', 22), bd=0,
    bg="#ffa64d", fg="black", insertbackground="black",
    width=14, justify='right', state='readonly'
)
entry.grid(row=0, column=0, columnspan=4, pady=15, padx=10)

button_bg = "#0059b3"
button_fg = "white"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'C':
        action = clear
    else:
        action = lambda t=text: press(t)

    tk.Button(
        root, text=text, padx=20, pady=20, font=('Arial', 14),
        bg=button_bg, fg=button_fg, bd=0, command=action
    ).grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

for i in range(6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
