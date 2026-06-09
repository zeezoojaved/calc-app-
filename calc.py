import tkinter as tk
from math import sin, cos, tan, sqrt, log10, radians
import turtle

# ---------------- CALCULATOR FUNCTIONS ---------------- #

expression = ""

def press(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

def scientific_function(func):
    global expression

    try:
        num = float(expression)

        if func == "sin":
            result = sin(radians(num))
        elif func == "cos":
            result = cos(radians(num))
        elif func == "tan":
            result = tan(radians(num))
        elif func == "sqrt":
            result = sqrt(num)
        elif func == "log":
            result = log10(num)

        expression = str(round(result, 8))
        entry_var.set(expression)

    except:
        entry_var.set("Error")
        expression = ""

# ---------------- TURTLE GRAPHICS ---------------- #

def draw_design():
    screen = turtle.Screen()
    screen.title("Turtle Design")

    pen = turtle.Turtle()
    pen.speed(0)

    for i in range(120):
        pen.forward(i * 2)
        pen.right(91)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x550")
root.resizable(False, False)

entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 20),
    justify="right"
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=15)

# Number and operator buttons

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text,row,col) in buttons:

    if text == '=':
        tk.Button(
            root,
            text=text,
            width=10,
            height=3,
            command=equal
        ).grid(row=row, column=col)
    else:
        tk.Button(
            root,
            text=text,
            width=10,
            height=3,
            command=lambda t=text: press(t)
        ).grid(row=row, column=col)

# Scientific Buttons

tk.Button(root, text="sin", width=10, height=3,
          command=lambda: scientific_function("sin")).grid(row=5, column=0)

tk.Button(root, text="cos", width=10, height=3,
          command=lambda: scientific_function("cos")).grid(row=5, column=1)

tk.Button(root, text="tan", width=10, height=3,
          command=lambda: scientific_function("tan")).grid(row=5, column=2)

tk.Button(root, text="√", width=10, height=3,
          command=lambda: scientific_function("sqrt")).grid(row=5, column=3)

tk.Button(root, text="log", width=10, height=3,
          command=lambda: scientific_function("log")).grid(row=6, column=0)

tk.Button(root, text="Clear", width=21, height=3,
          command=clear).grid(row=6, column=1, columnspan=2)

tk.Button(root, text="Turtle", width=10, height=3,
          command=draw_design).grid(row=6, column=3)

root.mainloop()