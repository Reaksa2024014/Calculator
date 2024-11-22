import sqlite3
# from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Combobox
# from datetime import date
# import pathlib


# # Create a new database or connect to an existing one
# conn = sqlite3.connect('students.db')
# c = conn.cursor()

# # Create the students table if it doesn't already exist
# c.execute('''CREATE TABLE IF NOT EXISTS students (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 reg_no TEXT,
#                 name TEXT,
#                 class TEXT,
#                 gender TEXT,
#                 dob TEXT,
#                 registration_date TEXT,
#                 religion TEXT,
#                 skill TEXT,
#                 father_name TEXT,
#                 mother_name TEXT,
#                 father_occupation TEXT,
#                 mother_occupation TEXT
#             )''')
# conn.commit()

# # Create the GUI window
# root = Tk()
# root.title("Student Registration System")
# root.geometry("800x950")
# root.config(bg="#06283D")

# def view_students():
#     c.execute("SELECT * FROM students")
#     students = c.fetchall()

#     student_list = Listbox(root)
#     student_list.pack()
#     for student in students:
#         student_list.insert(END, str(student))

# # Define the labels and entry fields
# def clear_entries():
#     reg_no_entry.delete(0, END)
#     name_entry.delete(0, END)
#     class_combobox.set('')
#     gender_combobox.set('')
#     dob_entry.delete(0, END)
#     religion_entry.set('')
#     skill_entry.delete(0, END)
#     father_name_entry.delete(0, END)
#     mother_name_entry.delete(0, END)
#     father_occupation_entry.delete(0, END)
#     mother_occupation_entry.delete(0, END)

# def register_student():
#     reg_no = reg_no_entry.get()
#     name = name_entry.get()
#     student_class = class_combobox.get()
#     gender = gender_combobox.get()
#     dob = dob_entry.get()
#     registration_date = date.today().strftime("%Y-%m-%d")
#     religion = religion_entry.get()
#     skill = skill_entry.get()
#     father_name = father_name_entry.get()
#     mother_name = mother_name_entry.get()
#     father_occupation = father_occupation_entry.get()
#     mother_occupation = mother_occupation_entry.get()

#     # Check if any of the fields are empty
#     if not reg_no or not name or not student_class or not gender or not dob:
#         messagebox.showwarning("Input Error", "Please fill all the required fields")
#         return

#     # Insert the student details into the database
#     c.execute('''INSERT INTO students (
#                     reg_no, name, class, gender, dob, registration_date, 
#                     religion, skill, father_name, mother_name, 
#                     father_occupation, mother_occupation) 
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
#                 (reg_no, name, student_class, gender, dob, registration_date, 
#                  religion, skill, father_name, mother_name, 
#                  father_occupation, mother_occupation))
#     conn.commit()

   
#     messagebox.showinfo("Success", "Student Registered Successfully")
#     clear_entries()

# # Create input fields for student data
# Label(root, text="Registration No.", bg='#06283D', fg='#fff').pack(pady=5)
# reg_no_entry = Entry(root, width=40)
# reg_no_entry.pack(pady=5)

# Label(root, text="Name", bg='#06283D', fg='#fff').pack(pady=5)
# name_entry = Entry(root, width=40)
# name_entry.pack(pady=5)

# Label(root, text="Class", bg='#06283D', fg='#fff').pack(pady=5)
# class_combobox = Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
# class_combobox.pack(pady=5)

# Label(root, text="Gender", bg='#06283D', fg='#fff').pack(pady=5)
# gender_combobox = Combobox(root, values=["Male", "Female"])
# gender_combobox.pack(pady=5)

# Label(root, text="Date of Birth", bg='#06283D', fg='#fff').pack(pady=5)
# dob_entry = Entry(root, width=40)
# dob_entry.pack(pady=5)

# Label(root, text="Religion", bg='#06283D', fg='#fff').pack(pady=5)
# religion_entry = Entry(root, width=40)
# religion_entry.pack(pady=5)

# Label(root, text="Skills", bg='#06283D', fg='#fff').pack(pady=5)
# skill_entry = Entry(root, width=40)
# skill_entry.pack(pady=5)

# Label(root, text="Father's Name", bg='#06283D', fg='#fff').pack(pady=5)
# father_name_entry = Entry(root, width=40)
# father_name_entry.pack(pady=5)

# Label(root, text="Mother's Name", bg='#06283D', fg='#fff').pack(pady=5)
# mother_name_entry = Entry(root, width=40)
# mother_name_entry.pack(pady=5)

# Label(root, text="Father's Occupation", bg='#06283D', fg='#fff').pack(pady=5)
# father_occupation_entry = Entry(root, width=40)
# father_occupation_entry.pack(pady=5)

# Label(root, text="Mother's Occupation", bg='#06283D', fg='#fff').pack(pady=5)
# mother_occupation_entry = Entry(root, width=40)
# mother_occupation_entry.pack(pady=5)


# # Add the view button (moved before register and footer)
# view_button = Button(root, text="View Students", command=view_students)
# view_button.pack(pady=10)

# # Register button
# register_button = Button(root, text="Register Student", bg='#5cb85c', fg='white', command=register_student)
# register_button.pack(pady=20)

# # Footer Information
# Label(root, text="Email: kyracksa@gmail.com", width=10, height=3, bg='#f0687c', anchor='e').pack(side=BOTTOM, fill=X)
# Label(root, text="STUDENT REGISTRATION", width=10, height=2, bg='#c36464', fg='#fff', font="arial 20 bold").pack(side=TOP, fill=X)

# # Start the Tkinter loop
# root.mainloop()

# # Close the database connection when done
# conn.close()








# from tkinter import Tk, Entry, Button, StringVar

# class Calculator:
#     def __init__(self, master):
#         master.title("Calculator")
#         master.geometry('357x420+0+0')
#         master.config(bg='gray')
#         master.resizable(False, False)

#         self.equation = StringVar()
#         self.entry_value = ""

#         Entry(width=17, bg="#ccddff", font=("Arial Bold", 28), textvariable=self.equation).place(x=0,y=0)

#         Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
#         Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
#         Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
#         Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
#         Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
#         Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
#         Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
#         Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
#         Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
#         Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
#         Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=90, y=275)
#         Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=180, y=275)
#         Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
#         Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
#         Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
#         Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
#         Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
#         Button(width=11, height=4, text='*', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
#         Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
#         Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)


#     def show(self, value):
#         self.entry_value += str(value)
#         self.equation.set(self.entry_value)

#     def clear(self):
#         self.entry_value = ""
#         self.equation.set(self.entry_value)

#     def solve(self):
#         result = eval(self.entry_value)
#         self.equation.set(result)

# root = Tk()
# calculator=Calculator(root)
# root.mainloop()


from tkinter import Tk, Entry, Button, StringVar, Frame
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        master.title("Scientific Calculator")
        master.geometry('430x685+0+0')
        master.config(bg='#2c2f33')
        master.resizable(True, True)

        self.equation = StringVar()
        self.entry_value = ""

        # Stylish Entry Widget
        entry = Entry(master, width=22, bg="#23272a", fg="white", font=("Arial", 24),
              textvariable=self.equation, bd=5, highlightthickness=0, justify='right') #.place(x=10, y=10)
        entry.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10, sticky="nsew")


        # Create a Frame for buttons
        button_frame = Frame(master, bg="#2c2f33")
        button_frame.place(x=10, y=80, width=410, height=570)

        # Configure grid weights for uniform distribution
        for i in range(7):  # 7 rows
            button_frame.rowconfigure(i, weight=1)  # Equal height for each row
        for j in range(4):  # 4 columns
            button_frame.columnconfigure(j, weight=1)  # Equal width for each column

        # Button configuration
        buttons = [
            ['C', '(', ')', '%'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', '=', '/'],
            ['sin', 'cos', 'tan','√'],
            ['!', 'log', 'e', '^'],
        ]

        colors = {'bg': '#7289da', 'fg': 'white', 'hover': '#99aab5'}

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                Button(button_frame, text=btn, font=("Arial", 18), bg=colors['bg'], fg=colors['fg'],
                       activebackground=colors['hover'], activeforeground="black",
                       relief='flat', height=2, width=6, command=lambda b=btn: self.on_button_click(b)).grid(row=i, column=j, padx=5, pady=5)

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
            elif button in ["sin", "cos", "tan"]:
                self.solve_advanced(button)
            elif button == "e":
                self.entry_value += str(math.e)
                self.equation.set(self.entry_value)
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
