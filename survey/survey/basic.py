# number = 10
# floating_point_number = 10.5
# text = "Hi!"
# bool_val = True
# print("Number is", number)
# print("Data type of number: ", type(number))
# print("Data type of number: ", type(floating_point_number))
# print("Data type of number: ", type(text))
# print("Data type of number: ", type(bool_val))
# print(number + 20)
# print(number * floating_point_number) dominant type




# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# weight = float(input("Enter your weight in meters: "))
# height = float(input("Enter your height in kg: "))
# BMI = weight / height ** 2
# print("Your body mass is", BMI )


# num1 = 10
# num2 = 3

# add = num1 + num2
# sub = num1 - num2
# mult = num1 * num2
# div = num1 / num2
# mod = num1 % num2
# floor_div = num1 // num2
# exp = num1 ** num2

# print("Addition result is", add)
# print("Substraction result is", sub)
# print("Multiplication result is", mult)
# print(f"Division result is {div:.2f}")
# print("Modulo result is", mod)
# print("Floor Division result is",floor_div)
# print("Exponential result is", exp)


# x = 10
# x += 10
# x += 10
# x += 10
# x += 10
# print(x)

# x = 10
# for i in range(4):
#     x += 10
# print(x)


# x = 10
# y = 3
# x += y
# print(x)
# x -= y
# print(x)
# x *= y
# print(x)
# x /= y
# print(x)
# x //= y
# print(x)
# x **= y
# print(x)
# x %=y
# print(x)



# price1 = float(input("Enter the price of item1: $"))
# qut1 = int(input("Enter the quantity of item1: $"))
# price2 = float(input("Enter the price of item2: $"))
# qut2 = int(input("Enter the quantity of item2: $"))
# price3 = float(input("Enter the price of item3: $"))
# qut3 = int(input("Enter the quantity of item3: $"))
# # total_cost = (price1 * qut1) + (price2 * qut2) + (price3 * qut3)

# total = 0
# total += price1 * qut1
# total += price2 * qut2
# total += price3 * qut3


# total += total * 0.1
# print(f"Total bill after tax: ${total:.2f}")
# print(f"Chance for a lucky draw: {total>100}")


# num1 = int(input("Enter the first number: "))
# num2 = int(input('Enter the second number: '))
# print("Input operation that you want to perform.")
# operation = input("Supported opperations are +,-,*,/,%,exp: ")

# if operation == "+":
#     print('Addition result is', num1+num2)
# elif operation == "-":
#     print('Substraction result is', num1-num2)
# elif operation == "*":
#     print('Multiplication result is', num1*num2)
# elif operation == "/":
#     print(f'Division result is{num1/num2:.2f}')
# elif operation == "%":
#     print('Modulo result is', num1%num2)
# elif operation == "exp":
#     print('Exponiantial result is', num1**num2)
# else:
#     print('Invalid input.')



# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print('It is an even number.')
# else:
#     print('It is an odd number.')



# saving = float(input('Enter the saving amount: '))

# if saving < 1000:
#     interest = 0.0
# elif 1000<=saving<=5000:
#     interest = 0.001
# elif 5000<saving<=10000:
#     interest = 0.002
# else:
#     interest = 0.0025

# interest_rate = saving * interest
# print(interest_rate)



# while True:
#     num1 = int(input('Input the first number: '))
#     num2 = int(input("Input the second number: "))
#     print("Input operation that you want to perform.")
#     operation = input('Supported operations are +,-,*,/,%,exp: ')
#     if operation == "+":
#         print("Addition result is", num1 +num2)
#     elif operation == "-":
#         print("Substracttion result is", num1 -num2)
#     elif operation == "*":
#         print("Multiplication result is", num1 *num2)
#     elif operation == "/":
#         print("Division result is", num1 /num2)
#     elif operation == "%":
#         print("Modulo result is", num1 %num2)
#     elif operation == "exp":
#         print("Exponiantial result is", num1 **num2)
#     else:
#         print("Invalid input.")
#     print("---")
#     cont = input("Type E to stop: ").lower()
#     if cont == 'e':
#         break
#     print("----")


# import random
# target_number = random.randint(1, 100)
# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100 with as less attempts as possible.")

# guess = int(input("Enter your guess: "))
# attempts = 1

# while guess != target_number:
#     if guess < target_number:
#         print("Too low!Try again.")
#     elif guess > target_number:
#         print("Too high!Try again")

#     guess = int(input("Enter your guess: "))
#     attempts += 1

# print(f"Congratulations! You guessed the number in {attempts} attempts.")



# import random
# target_number = random.randint(1, 100)
# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100 with as less attempts as possible.")

# guess = int(input("Enter your guess: "))
# attempts = 1

# while guess != target_number and attempts < 7:
#     if guess < target_number:
#         print("Too low!Try again.")
#     elif guess > target_number:
#         print("Too high!Try again")

#     guess = int(input("Enter your guess: "))
#     attempts += 1
# if guess == target_number:
#     print(f"Congratulations! You guessed the number in {attempts} attempts.")
# else:
#     print(f"Maximum attempts of {attempts}.Game Over!")



# for i in range(10):
#     print(i)

# print("Generate odd number from 1-9: ")
# for i in range(1, 10, 2):
#     print(i)


# print("Generate 10 odd number: ")
# odd_num = 1
# for i in range(10):
#     print(odd_num)
#     odd_num += 2


# student = 10
# for i in range(student):
#     score = int(input("Input score: "))

#     if score >= 90:
#         grade = "A"
#     elif score > 80:
#         grade = "B"
#     else:
#         grade = "C"
#     print(f"Student {i} got grade {grade}")



# start = int(input("Enter starting range: "))
# stop = int(input("Enter stopping range: "))
# sum = 0
# for i in range(start, stop + 1):
#     sum += i
# print(sum)





# def calculate_interest(savings):
#  # Determine the interest rate based on the saving amount
#     if savings < 1000:
#         interest_rate = 0.0
#     elif savings <= 5000:
#         interest_rate = 0.001 # 0.1%
#     elif savings <= 10000:
#         interest_rate = 0.002 # 0.2%
#     else:
#         interest_rate = 0.0025 # 0.25%
#     # Calculate the interest
#     interest = savings * interest_rate
#     return interest
# savings_amount = 5000
#     # Calling the function
# print(calculate_interest(savings_amount))
# print("Your current balance = $", savings_amount + calculate_interest(savings_amount))



#Database with python

import sqlite3
# Connect to database (creates file if not exists)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                     id INTEGER PRIMARY KEY,
                     name TEXT,
                     enrollmentdate DATE
              )''')

cursor.execute("INSERT INTO Students (name, enrollmentdate) VALUES ('Alice', '2024-07-03')")
cursor.execute("INSERT INTO Students (name, enrollmentdate) VALUES (‘Bob', '2024-07-05')")
conn.commit() # Save changes

cursor.execute("SELECT * FROM Students")
results = cursor.fetchall() # Fetch all records
for row in results:
    print(row)
conn.close() # Close the connection when done

while True:
    print("1. Type 1 to Insert data.")
    print("2. Type 2 to Output all data.")
    print("3. Type 3 to exit the program.")
    cmd = int(input("Type here: "))
    print("---")
    if cmd == 1:
        name = input("Input student's name: ")
        date = input("Input enrollment's date: ")
        cursor.execute(f"INSERT INTO Students (name, enrollmentdate) VALUES ('{name}', '{date}')")
        conn.commit() # Save changes
    if cmd == 2:
        cursor.execute("SELECT * FROM Students")
        results = cursor.fetchall() # Fetch all records
    for row in results:
        print(row)
    if cmd == 3:









        
        break
    print("---")
conn.close() # Close the connection when done



