# """
#   comparasion operator
#   1. `==`: is equal to
#   2. `<` : less than
#   3. `>` : greater than
#   4. `>=` : greater than or equal to
#   5. `<=` : less than or equal to
#   6. `!=` : not equal to 

# """
# print("-"*10 + "is equal to `=`" + "-"*10)
# print(f"5 is equal to 5? {5==5}")
# print(f"10 is equal to 15 {10==15}")


# print('\n', "#"* 40)
# print("-"*40)
# print()
# print("-"*10 + "less than`<`" + "-"*10 )
# print(f"0 is less than 0? {0<0}")
# print(f'5 is less than 10? {5 < 0}')
# print(f"3 is less than 2? {3<2}")



# print(2020<= 2021-1) #T
# print(5*3<= 3*5)#T
# print(6**2 <= 2**6)#T



# x= 3
# y= 5
# print(x<=y) #T
# print(x*y<=y*x) #T


# # A = 5 * 10 / 2
# # B = 8 * 12 /2
# # print(A<=B) #T
# print(5 * 10/ 2 <=  8*12/2)


# ch = chr(65)
# print(ch)

# c = ord("a")
# print(c)
# or
# print(ord("A"))


#logical operators
    # 1. and 
    # 2. or
    # 3. not

# print("apple") and 5 >2
# print(3 > 3 and "java")













# print(print()) #none

# print("show something") and print("programming is about thinking") #show something
# not print("show something") and print("programming is about thinking")# false

# a = 20 and 10
# print(a)

#or
# user_input = "I am so lazy."
# result = user_input or "This user don't input anything!"
# print(result)

# print(not not 8)
# print( "baby" and 8 )

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# a = float(input("Enter a: ")) 
# # b = eval(input("Enter b: "))  can do calculate. 
# c = int(input("Enter c: "))






# x = 456
# remain = x % 10 #6
# result1 = remain * 10
# x //= 10 #45 new x = 45
# reverse = (result1 + (x % 10)) * 10 + (x // 10) 
# print(reverse)





# x = 456
# reverse = x % 10 #6
# x //= 10 #45
# reverse = ((reverse * 10) + (x % 10))* 10 + (x//10)
# print(reverse)










# odd or even

# show x is odd or even​​​​​​ teacher
# x = 11
# result = (x % 2 == 0 and "even") or "odd"
# print(result)





# x = 456
# reverse = x % 10 #6
# x //= 10 #45
# b = x % 10
# c = x // 10
# result = ((reverse * 10) + b) * 10 + c
# print(result)


#this is my code
# x = 1234
# a = x % 10 #4
# x //= 10 #123 new x = 123
# b = x //10 #12

# result = (((a * 10) + (x % 10)) * 10 + (b % 10))* 10 + (b // 10)
# print(result)

# i =  1
# while i < 10:
#     print(i)
#     i = i + 1


# for i in range(1, 10, 2):
#     print()
#     for j in range(1, 10, 2):
#         print(f"{i*j}""", end=" ")



# def max(num1, num2):
#     if num1 > num2:
#         result = num1
#     else:
#         result = num2
#     return result 
# def main():
#     i = 5
#     j = 2
#     k = min(i, j)
#     print(f"The smaller number of {i} and {j} is {k}")
# main()




# None return function no perimeter
# def my_function():
#     print("I love you baby.")
# my_function()

#None return function with perimeter
# def my_function(a):
#     print(a)
# my_function(5)

#Return function no perimmeter
# def my_function():
#     return "I love you baby."
# print(my_function())

#Return function with perimeter
# def my_function(a):
#     return a
# print(my_function(5))

# local scope
# def my_function():
#     local_var = "I am local"
#     print(local_var)
# my_function()

#Global scope
# global_var = "Hello idol"

# def my_function():
#     print(global_var)
# my_function()

#Enclosing scope(Nonlocal)
# def outer_function():
#     outer_var = "Original value"
    
#     def inner_function():
        

# secret_number = 42
# guess = 0
# while guess != secret_number:
#     guess = int(input("Guess the secret number: "))
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
# print("Congratulations, you guessed it!")

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         # i += 1
#         continue
  
#     print(i)
    # i += 1


# count = 0
# for x in range(100,1000):
#     if x % 5 == 0 and x % 6 == 0:
#         print(x, end=' ')
#         count += 1
#         if count % 10 == 0:
#             print()

# def outer_function():
#     outer_var = "Original value"

#     def inner_function():
#         nonlocal outer_var
#         outer_var = "Modified value"

#     inner_function()
#     print(outer_var)
# outer_function()

# def multiplication_function():
#     num = int(input("Enter a number: "))
#     multiplier = 1
#     print("multiplication table of", num)
#     while multiplier <= 10:
#         print(num, "X", multiplier, "=" , num * multiplier)
#         multiplier+=1
# # multiplication_function()


# def addition_function():
#     num = int(input("addition function, : "))
#     adder = 1
#     print("addition table of", num)
#     while adder <= 10:
#         print(num, "+", adder, "=" , num + adder)
#         adder+=1

# def subtraction_fuction():
#     num = int(input("Enter a number: "))
#     minusValue = 1
#     print("addition table of", num)
#     while minusValue <= 10:
#         print(num, "-", minusValue, "=" , minusValue - num )
#         minusValue+=1


# def subtraction_fuction():
#     num = int(input("Enter a number: "))
#     divisibleValue = 1
#     print("addition table of", num)
#     while divisibleValue <= 10:
#         print(num, "/", divisibleValue, "=" , divisibleValue / num)
#         divisibleValue+=1



# def Even_Odd_Checking():
#     for i in range(3):
#         number = int(input('Enter a number: '))
#         if number % 2 == 0:
#             print(f"{number} is Even")
#         else:
#             print(f"{number} is Odd")

# Even_Odd_Checking()



# def Rock_Paper_Scissors():
#     for i in range(3):
#         player_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#         computer_choice = "rock"

#         if player_choice == computer_choice:
#             print("It's a tie!")
#         elif (player_choice == "rock" and computer_choice == "scissors") or \
#             (player_choice == "scissors" and computer_choice == "paper") or \
#             (player_choice == "paper" and computer_choice == "rock"):
#             print("You win!")
#         else:
#             print("You lose!")
# Rock_Paper_Scissors()


# def adult_minor():
#     for i in range(3):
#         age = int(input("Enter your age: "))
#         if age >= 18:
#             print("You are an adult.")
#         else:
#             print("You are a minor")
# adult_minor()



import tkinter as tk
from tkinter import ttk, messagebox

def binaryToDecimal(binaryValue):
    decimal = 0
    power = 0
    for digit in reversed(binaryValue):
        if digit not in '01':
            raise ValueError("Invalid binary digit")
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

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

def decimalToOctal(decimalValue):
    octal = ""
    while decimalValue != 0:
        octalValue = decimalValue % 8
        octal = octalDigit(octalValue) + octal
        decimalValue = decimalValue // 8
    return octal if octal else "0"

def octalToDecimal(octalValue):
    decimal = 0
    power = 0
    for digit in reversed(octalValue):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit")
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal

def hexadecimalToBinary(hexadecimalValue):
    decimalValue = int(hexadecimalValue, 16)
    return decimalToBinary(decimalValue)

def binaryToHexadecimal(binaryValue):
    decimalValue = binaryToDecimal(binaryValue)
    hexadecimal = ""
    if decimalValue == 0:
        return "0"
    while decimalValue != 0:
        hexValue = decimalValue % 16
        hexadecimal = hexDigit(hexValue) + hexadecimal
        decimalValue = decimalValue // 16
    return hexadecimal

def octalDigit(octalValue):
    if 0 <= octalValue <= 7:
        return chr(octalValue + ord('0'))

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
            result = binaryToDecimal(input_value)
        elif conversion_type == "Decimal to Binary":
            result = decimalToBinary(int(input_value))
        elif conversion_type == "Decimal to Octal":
            result = decimalToOctal(int(input_value))
        elif conversion_type == "Octal to Decimal":
            result = octalToDecimal(input_value)
        elif conversion_type == "Hexadecimal to Binary":
            result = hexadecimalToBinary(input_value)
        elif conversion_type == "Binary to Hexadecimal":
            result = binaryToHexadecimal(input_value)
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













