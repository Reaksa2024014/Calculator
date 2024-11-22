from tkinter import Tk, Entry, Button, StringVar, Frame
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        master.title("Scientific Calculator")
        master.geometry('430x760+0+0')  # Adjusted height
        master.config(bg='#2c2f33')
        master.resizable(True, True)

        self.equation = StringVar()
        self.entry_value = ""

        # Stylish Entry Widget
        entry = Entry(master, width=22, bg="#23272a", fg="white", font=("Arial", 24),
                      textvariable=self.equation, bd=5, highlightthickness=0, justify='right')
        entry.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10, sticky="nsew")

        # Create a Frame for buttons
        button_frame = Frame(master, bg="#2c2f33")
        button_frame.place(x=10, y=80, width=410, height=600)

        # Configure grid weights for uniform distribution
        for i in range(8):  # Updated to 8 rows
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):  # 4 columns
            button_frame.columnconfigure(j, weight=1)

        # Button configuration
        buttons = [
            ['C', '(', ')', '%'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', '=', '/'],
            ['sin', 'cos', 'tan', '√'],
            ['!', 'log', 'ln', '^'],
            ['rad', 'deg', 'π', 'e'],
        ]

        colors = {'bg': '#7289da', 'fg': 'white', 'hover': '#99aab5'}

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                Button(button_frame, text=btn, font=("Arial", 18), bg=colors['bg'], fg=colors['fg'],
                       activebackground=colors['hover'], activeforeground="black",
                       relief='flat', height=2, width=6,  # Button height and width
                       command=lambda b=btn: self.on_button_click(b)).grid(row=i, column=j, padx=5, pady=5)

    def on_button_click(self, button):
        try:
            if button == "C":
                self.clear()
            elif button == "=":
                self.solve()
            elif button == "^":
                self.entry_value += "**"
                self.equation.set(self.entry_value)
            elif button == "√":
                self.solve_advanced("sqrt")
            elif button == "log":
                self.solve_advanced("log")
            elif button == "ln":
                self.solve_advanced("ln")
            elif button == "rad":
                self.solve_advanced("rad")
            elif button == "deg":
                self.solve_advanced("deg")
            elif button == "π":
                self.entry_value += str(math.pi)
                self.equation.set(self.entry_value)
            elif button == "e":
                self.entry_value += str(math.e)
                self.equation.set(self.entry_value)
            elif button in ["sin", "cos", "tan"]:
                self.solve_advanced(button)
            elif button == "!":
                self.solve_advanced("factorial")
            else:
                self.show(button)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Operation")

    def solve_advanced(self, operation):
        try:
            if self.entry_value == "":
                raise ValueError("Empty Input")
            value = float(self.entry_value)

            if operation == "sqrt":
                result = math.sqrt(value)
            elif operation == "log":
                result = math.log10(value)
            elif operation == "ln":
                result = math.log(value)  # Natural log
            elif operation == "rad":
                result = math.radians(value)  # Degrees to radians
            elif operation == "deg":
                result = math.degrees(value)  # Radians to degrees
            elif operation == "factorial":
                if not value.is_integer() or value < 0:
                    raise ValueError("Factorial undefined for non-integer or negative values")
                result = math.factorial(int(value))
            elif operation == "sin":
                result = math.sin(math.radians(value))
            elif operation == "cos":
                result = math.cos(math.radians(value))
            elif operation == "tan":
                result = math.tan(math.radians(value))

            self.equation.set(result)
            self.entry_value = str(result)
        except ValueError:
            self.equation.set("Error")
            self.entry_value = ""

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
