

# class convertionApplication:
# # Binary to Decimal conversion
#     def binary_to_decimal(binary_str):
#         try:
#             return int(binary_str, 2)
#         except ValueError:
#             return "Invalid binary number"

#     # Decimal to Binary conversion
#     def decimal_to_binary(decimal_num):
#         try:
#             return bin(decimal_num).replace("0b", "")
#         except ValueError:
#             return "Invalid decimal number"

#     # Hexadecimal to Octal conversion
#     def hexadecimal_to_octal(hex_str):
#         try:
#             decimal_value = int(hex_str, 16)
#             return oct(decimal_value).replace("0o", "")
#         except ValueError:
#             return "Invalid hexadecimal number"

#     # Decimal to Octal conversion
#     def decimal_to_octal(decimal_num):
#         try:
#             return oct(decimal_num).replace("0o", "")
#         except ValueError:
#             return "Invalid decimal number"

#     # Octal to Decimal conversion
#     def octal_to_decimal(octal_str):
#         try:
#             return int(octal_str, 8)
#         except ValueError:
#             return "Invalid octal number"

#     # Hexadecimal to Binary conversion
#     def hexadecimal_to_binary(hex_str):
#         try:
#             decimal_value = int(hex_str, 16)
#             return bin(decimal_value).replace("0b", "")
#         except ValueError:
#             return "Invalid hexadecimal number"

#     # Binary to Hexadecimal conversion
#     def binary_to_hexadecimal(binary_str):
#         try:
#             decimal_value = int(binary_str, 2)
#             return hex(decimal_value).replace("0x", "").upper()
#         except ValueError:
#             return "Invalid binary number"

#     # Main function to handle user input and conversions
#     def main():
        
#         obj1 = convertionApplication()
        
#         while True:
#             print("\nChoose a conversion option:")
#             print("1. Binary to Decimal")
#             print("2. Decimal to Binary")
#             print("3. Hexadecimal to Octal")
#             print("4. Decimal to Octal")
#             print("5. Octal to Decimal")
#             print("6. Hexadecimal to Binary")
#             print("7. Binary to Hexadecimal")
#             print("8. Exit")

#             choice = input("Enter your choice (1-8): ")

#             if choice == "1":
#                 binary_str = input("Enter a binary number: ")
#                 result = obj1.binary_to_decimal(binary_str)
#                 print(f"Binary {binary_str} to Decimal is {result}")

#             elif choice == "2":
#                 decimal_num = int(input("Enter a decimal number: "))
#                 result = obj1.decimal_to_binary(decimal_num)
#                 print(f"Decimal {decimal_num} to Binary is {result}")

#             elif choice == "3":
#                 hex_str = input("Enter a hexadecimal number: ")
#                 result = obj1.hexadecimal_to_octal(hex_str)
#                 print(f"Hexadecimal {hex_str} to Octal is {result}")

#             elif choice == "4":
#                 decimal_num = int(input("Enter a decimal number: "))
#                 result = obj1.decimal_to_octal(decimal_num)
#                 print(f"Decimal {decimal_num} to Octal is {result}")

#             elif choice == "5":
#                 octal_str = input("Enter an octal number: ")
#                 result = obj1.octal_to_decimal(octal_str)
#                 print(f"Octal {octal_str} to Decimal is {result}")

#             elif choice == "6":
#                 hex_str = input("Enter a hexadecimal number: ")
#                 result = obj1.hexadecimal_to_binary(hex_str)
#                 print(f"Hexadecimal {hex_str} to Binary is {result}")

#             elif choice == "7":
#                 binary_str = input("Enter a binary number: ")
#                 result = obj1.binary_to_hexadecimal(binary_str)
#                 print(f"Binary {binary_str} to Hexadecimal is {result}")

#             elif choice == "8":
#                 print("Exiting the program.")
#                 break

#             else:
#                 print("Invalid choice. Please try again.")

#     if __name__ == "__main__":
#         main()








# import tkinter as tk
# from tkinter import messagebox

# # Conversion functions
# def binary_to_decimal(binary_str):
#     try:
#         return int(binary_str, 2)
#     except ValueError:
#         return "Invalid binary number"

# def decimal_to_binary(decimal_num):
#     try:
#         return bin(decimal_num).replace("0b", "")
#     except ValueError:
#         return "Invalid decimal number"

# def hexadecimal_to_octal(hex_str):
#     try:
#         decimal_value = int(hex_str, 16)
#         return oct(decimal_value).replace("0o", "")
#     except ValueError:
#         return "Invalid hexadecimal number"

# def decimal_to_octal(decimal_num):
#     try:
#         return oct(decimal_num).replace("0o", "")
#     except ValueError:
#         return "Invalid decimal number"

# def octal_to_decimal(octal_str):
#     try:
#         return int(octal_str, 8)
#     except ValueError:
#         return "Invalid octal number"

# def hexadecimal_to_binary(hex_str):
#     try:
#         decimal_value = int(hex_str, 16)
#         return bin(decimal_value).replace("0b", "")
#     except ValueError:
#         return "Invalid hexadecimal number"

# def binary_to_hexadecimal(binary_str):
#     try:
#         decimal_value = int(binary_str, 2)
#         return hex(decimal_value).replace("0x", "").upper()
#     except ValueError:
#         return "Invalid binary number"

# # Function to handle conversion based on user's choice
# def convert():
#     input_value = entry.get().strip()
#     if conversion_var.get() == 1:  # Binary to Decimal
#         result = binary_to_decimal(input_value)
#     elif conversion_var.get() == 2:  # Decimal to Binary
#         result = decimal_to_binary(int(input_value))
#     elif conversion_var.get() == 3:  # Hexadecimal to Octal
#         result = hexadecimal_to_octal(input_value)
#     elif conversion_var.get() == 4:  # Decimal to Octal
#         result = decimal_to_octal(int(input_value))
#     elif conversion_var.get() == 5:  # Octal to Decimal
#         result = octal_to_decimal(input_value)
#     elif conversion_var.get() == 6:  # Hexadecimal to Binary
#         result = hexadecimal_to_binary(input_value)
#     elif conversion_var.get() == 7:  # Binary to Hexadecimal
#         result = binary_to_hexadecimal(input_value)
#     else:
#         result = "Invalid choice"

#     result_label.config(text=f"Result: {result}")

# # Setting up the UI window
# root = tk.Tk()
# root.title("Number Conversion")

# # Input field and label
# tk.Label(root, text="Enter the number:").grid(row=0, column=0, padx=10, pady=10)
# entry = tk.Entry(root, width=30)
# entry.grid(row=0, column=1, padx=10, pady=10)

# # Radio buttons for selecting conversion type
# conversion_var = tk.IntVar()

# tk.Radiobutton(root, text="Binary to Decimal", variable=conversion_var, value=1).grid(row=1, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Decimal to Binary", variable=conversion_var, value=2).grid(row=2, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Hexadecimal to Octal", variable=conversion_var, value=3).grid(row=3, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Decimal to Octal", variable=conversion_var, value=4).grid(row=4, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Octal to Decimal", variable=conversion_var, value=5).grid(row=5, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Hexadecimal to Binary", variable=conversion_var, value=6).grid(row=6, column=0, padx=10, pady=5)
# tk.Radiobutton(root, text="Binary to Hexadecimal", variable=conversion_var, value=7).grid(row=7, column=0, padx=10, pady=5)

# # Button to trigger conversion
# convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.grid(row=8, column=0, columnspan=2, pady=10)

# # Label to display result
# result_label = tk.Label(root, text="Result: ")
# result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# # Start the UI loop
# root.mainloop()




# class ConvertionApplication:
#     # Binary to Decimal conversion
#     @staticmethod
#     def binary_to_decimal(binary_str):
#         try:
#             return int(binary_str, 2)
#         except ValueError:
#             return "Invalid binary number"

#     # Decimal to Binary conversion
#     @staticmethod
#     def decimal_to_binary(decimal_num):
#         try:
#             return bin(decimal_num).replace("0b", "")
#         except ValueError:
#             return "Invalid decimal number"

#     # Hexadecimal to Octal conversion
#     @staticmethod
#     def hexadecimal_to_octal(hex_str):
#         try:
#             decimal_value = int(hex_str, 16)
#             return oct(decimal_value).replace("0o", "")
#         except ValueError:
#             return "Invalid hexadecimal number"

#     # Decimal to Octal conversion
#     @staticmethod
#     def decimal_to_octal(decimal_num):
#         try:
#             return oct(decimal_num).replace("0o", "")
#         except ValueError:
#             return "Invalid decimal number"

#     # Octal to Decimal conversion
#     @staticmethod
#     def octal_to_decimal(octal_str):
#         try:
#             return int(octal_str, 8)
#         except ValueError:
#             return "Invalid octal number"

#     # Hexadecimal to Binary conversion
#     @staticmethod
#     def hexadecimal_to_binary(hex_str):
#         try:
#             decimal_value = int(hex_str, 16)
#             return bin(decimal_value).replace("0b", "")
#         except ValueError:
#             return "Invalid hexadecimal number"

#     # Binary to Hexadecimal conversion
#     @staticmethod
#     def binary_to_hexadecimal(binary_str):
#         try:
#             decimal_value = int(binary_str, 2)
#             return hex(decimal_value).replace("0x", "").upper()
#         except ValueError:
#             return "Invalid binary number"

#     # Main function to handle user input and conversions
#     @staticmethod
#     def main():
#         while True:
#             print("\nChoose a conversion option:")
#             print("1. Binary to Decimal")
#             print("2. Decimal to Binary")
#             print("3. Hexadecimal to Octal")
#             print("4. Decimal to Octal")
#             print("5. Octal to Decimal")
#             print("6. Hexadecimal to Binary")
#             print("7. Binary to Hexadecimal")
#             print("8. Exit")

#             choice = input("Enter your choice (1-8): ")

#             if choice == "1":
#                 binary_str = input("Enter a binary number: ")
#                 result = ConvertionApplication.binary_to_decimal(binary_str)
#                 print(f"Binary {binary_str} to Decimal is {result}")

#             elif choice == "2":
#                 decimal_num = int(input("Enter a decimal number: "))
#                 result = ConvertionApplication.decimal_to_binary(decimal_num)
#                 print(f"Decimal {decimal_num} to Binary is {result}")

#             elif choice == "3":
#                 hex_str = input("Enter a hexadecimal number: ")
#                 result = ConvertionApplication.hexadecimal_to_octal(hex_str)
#                 print(f"Hexadecimal {hex_str} to Octal is {result}")

#             elif choice == "4":
#                 decimal_num = int(input("Enter a decimal number: "))
#                 result = ConvertionApplication.decimal_to_octal(decimal_num)
#                 print(f"Decimal {decimal_num} to Octal is {result}")

#             elif choice == "5":
#                 octal_str = input("Enter an octal number: ")
#                 result = ConvertionApplication.octal_to_decimal(octal_str)
#                 print(f"Octal {octal_str} to Decimal is {result}")

#             elif choice == "6":
#                 hex_str = input("Enter a hexadecimal number: ")
#                 result = ConvertionApplication.hexadecimal_to_binary(hex_str)
#                 print(f"Hexadecimal {hex_str} to Binary is {result}")

#             elif choice == "7":
#                 binary_str = input("Enter a binary number: ")
#                 result = ConvertionApplication.binary_to_hexadecimal(binary_str)
#                 print(f"Binary {binary_str} to Hexadecimal is {result}")

#             elif choice == "8":
#                 print("Exiting the program.")
#                 break

#             else:
#                 print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     ConvertionApplication.main()





import tkinter as tk
from tkinter import ttk, messagebox
class convertionApplication:

    @staticmethod
    def binaryToDecimal(binaryValue):
        decimal = 0
        power = 0
        for digit in reversed(binaryValue):
            if digit not in '01':
                raise ValueError("Invalid binary digit")
            decimal += int(digit) * (2 ** power)
            power += 1
        return decimal

    @staticmethod
    def decimalToBinary(decimalValue):
        if decimalValue < 0:
            raise ValueError("Decimal value must be non-negative")
        binary = ""
        if decimalValue == 0:
            return "0"
        while decimalValue != 0:
            binary = str(decimalValue % 2) + binary
            decimalValue = decimalValue // 2
        return binary
    
    @staticmethod
    def decimalToOctal(decimalValue):
        octal = ""
        while decimalValue != 0:
            octalValue = decimalValue % 8
            octal = convertionApplication.octalDigit(octalValue) + octal
            decimalValue = decimalValue // 8
        return octal if octal else "0"

    @staticmethod
    def octalToDecimal(octalValue):
        decimal = 0
        power = 0
        for digit in reversed(octalValue):
            if digit not in '01234567':
                raise ValueError("Invalid octal digit")
            decimal += int(digit) * (8 ** power)
            power += 1
        return decimal
    @staticmethod
    def hexadecimalToBinary(hexadecimalValue):
        decimalValue = int(hexadecimalValue, 16)
        return convertionApplication.decimalToBinary(decimalValue)
    @staticmethod
    def binaryToHexadecimal(binaryValue):
        decimalValue = convertionApplication.binaryToDecimal(binaryValue)
        hexadecimal = ""
        if decimalValue == 0:
            return "0"
        while decimalValue != 0:
            hexValue = decimalValue % 16
            hexadecimal = convertionApplication.hexDigit(hexValue) + hexadecimal
            decimalValue = decimalValue // 16
        return hexadecimal
    @staticmethod
    def octalDigit(octalValue):
        if 0 <= octalValue <= 7:
            return chr(octalValue + ord('0'))
    @staticmethod
    def hexDigit(hexValue):
        if 0 <= hexValue <= 9:
            return chr(hexValue + ord('0'))
        elif 10 <= hexValue <= 15:
            return chr(hexValue - 10 + ord('A'))
        raise ValueError("Invalid hex value")

def convert():
        input_value = entry.get()
        conversion_type = combo.get()
    
        try:
            if conversion_type == "Binary to Decimal":
                result = convertionApplication.binaryToDecimal(input_value)
            elif conversion_type == "Decimal to Binary":
                result = convertionApplication.decimalToBinary(int(input_value))
            elif conversion_type == "Decimal to Octal":
                result = convertionApplication.decimalToOctal(int(input_value))
            elif conversion_type == "Octal to Decimal":
                result = convertionApplication.octalToDecimal(input_value)
            elif conversion_type == "Hexadecimal to Binary":
                result = convertionApplication.hexadecimalToBinary(input_value)
            elif conversion_type == "Binary to Hexadecimal":
                result = convertionApplication.binaryToHexadecimal(input_value)
            else:
                raise ValueError("Invalid conversion type")
        
            result_entry.delete(0, tk.END)
            result_entry.insert(0, str(result))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Create the main window
root = tk.Tk()
root.title("Number Base Converter")

    # Create and place the input field
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

    # Create and place the label for the input field
label = tk.Label(root, text="Enter number:")
label.grid(row=0, column=0)

    # Create and place the dropdown menu for conversion types
conversion_types = [
        "Binary to Decimal",
        "Decimal to Binary",
        "Decimal to Octal",
        "Octal to Decimal",
        "Hexadecimal to Binary",
        "Binary to Hexadecimal"
    ]
combo = ttk.Combobox(root, values=conversion_types, state="readonly")
combo.grid(row=1, column=1, padx=10, pady=10)
combo.set("Select Conversion Type")

# Create and place the Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0)

# Create and place the result field
result_entry = tk.Entry(root, width=30)
result_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the label for the result field
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0)

# Run the application
root.mainloop()