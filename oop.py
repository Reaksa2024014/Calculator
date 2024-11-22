# import tkinter as tk
# from tkinter import ttk, messagebox

# class convertionApplication:
#     def binaryToDecimal(self, binaryValue):
#         decimal = 0
#         power = 0
#         for digit in reversed(binaryValue):
#             if digit not in '01':
#                 raise ValueError("Invalid binary digit")
#             decimal += int(digit) * (2 ** power)
#             power += 1
#         return decimal

#     def decimalToBinary(self, decimalValue):
#         if decimalValue < 0:
#             raise ValueError("Decimal value must be non-negative")
#         binary = ""
#         if decimalValue == 0:
#             return "0"
#         while decimalValue != 0:
#             binary = str(decimalValue % 2) + binary
#             decimalValue = decimalValue // 2
#         return binary

#     def decimalToOctal(self, decimalValue):
#         octal = ""
#         while decimalValue != 0:
#             octalValue = decimalValue % 8
#             octal = self.octalDigit(octalValue) + octal
#             decimalValue = decimalValue // 8
#         return octal if octal else "0"

#     def octalToDecimal(self, octalValue):
#         decimal = 0
#         power = 0
#         for digit in reversed(octalValue):
#             if digit not in '01234567':
#                 raise ValueError("Invalid octal digit")
#             decimal += int(digit) * (8 ** power)
#             power += 1
#         return decimal

#     def hexadecimalToBinary(self, hexadecimalValue):
#         decimalValue = int(hexadecimalValue, 16)
#         return self.decimalToBinary(decimalValue)

#     def binaryToHexadecimal(self, binaryValue):
#         decimalValue = self.binaryToDecimal(binaryValue)
#         hexadecimal = ""
#         if decimalValue == 0:
#             return "0"
#         while decimalValue != 0:
#             hexValue = decimalValue % 16
#             hexadecimal = self.hexDigit(hexValue) + hexadecimal
#             decimalValue = decimalValue // 16
#         return hexadecimal

#     def octalDigit(self, octalValue):
#         if 0 <= octalValue <= 7:
#             return chr(octalValue + ord('0'))

#     def hexDigit(self, hexValue):
#         if 0 <= hexValue <= 9:
#             return chr(hexValue + ord('0'))
#         elif 10 <= hexValue <= 15:
#             return chr(hexValue - 10 + ord('A'))
#         raise ValueError("Invalid hex value")

# def convert():
#     input_value = entry.get()
#     conversion_type = combo.get()
    
#     try:
#         if conversion_type == "Binary to Decimal":
#             result = object1.binaryToDecimal(input_value)
#         elif conversion_type == "Decimal to Binary":
#             result = object1.decimalToBinary(int(input_value))
#         elif conversion_type == "Decimal to Octal":
#             result = object1.decimalToOctal(int(input_value))
#         elif conversion_type == "Octal to Decimal":
#             result = object1.octalToDecimal(input_value)
#         elif conversion_type == "Hexadecimal to Binary":
#             result = object1.hexadecimalToBinary(input_value)
#         elif conversion_type == "Binary to Hexadecimal":
#             result = object1.binaryToHexadecimal(input_value)
#         else:
#             raise ValueError("Invalid conversion type")
       
#         result_entry.delete(0, tk.END)
#         result_entry.insert(0, str(result))
#     except ValueError as e:
#         messagebox.showerror("Error", str(e))

# # Create the main window
# root = tk.Tk()
# root.title("Number Base Converter")

# # Create and place the input field
# entry = tk.Entry(root, width=30)
# entry.grid(row=0, column=1, padx=10, pady=10)

# # Create and place the label for the input field
# label = tk.Label(root, text="Enter number:")
# label.grid(row=0, column=0)

# # Create and place the dropdown menu for conversion types
# conversion_types = [
#     "Binary to Decimal",
#     "Decimal to Binary",
#     "Decimal to Octal",
#     "Octal to Decimal",
#     "Hexadecimal to Binary",
#     "Binary to Hexadecimal"
# ]
# combo = ttk.Combobox(root, values=conversion_types, state="readonly")
# combo.grid(row=1, column=1, padx=10, pady=10)
# combo.set("Select Conversion Type")

# # Create and place the Convert button
# convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.grid(row=1, column=0)

# # Create and place the result field
# result_entry = tk.Entry(root, width=30)
# result_entry.grid(row=2, column=1, padx=10, pady=10)

# # Create and place the label for the result field
# result_label = tk.Label(root, text="Result:")
# result_label.grid(row=2, column=0)

# # Create an instance of convertionApplication
# object1 = convertionApplication()

# # Run the application
# root.mainloop()









# class Car:
#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print("This "+ self.model+" is driving")

#     def stop(self):
#         print("This "+ self.model+" is stopped")


