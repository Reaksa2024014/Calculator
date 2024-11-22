#casting
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are teenager.")
# if age >= 18 and age <= 65:
#     print("You are adult.")
# if age > 65:
#     print("You are elder.")


# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are teenager.")
# else:
#     print("You are older than me.")

# import os
# answer = input("Do you want to go to the cinema? yes/no: ").lower()
# if answer == "yes":
#     print("Let's go!")
# # else:
# #     print("I am really disappionted to hear that.")
# else:
#     os.system("shutdown /s /f /t 5") #shutdown 5 second. 


#delete folder
# import shutil
# shutil.rmtree("c:\\loop") #delete folder file



a = 10
b = 10
c = 50

if a > b and a > c:
    print("A is the maximum number.")
elif b > a and b > c:
    print("b is the maximum number")
else:
    print("c is the maximum number")



# a = 100
# b = 200
# c = 300
# my_max = a
# if my_max < b: my_max = b
# if my_max < c: my_max = c
# print(my_max)   #the output is the number.

# a = 100
# b = 200
# c = 300
# my_max = a
# if my_max < b: my_max = b
# if my_max < c: my_max = c



# a = 800
# b = 900
# c = 1000
# # my_max = "a"
# # if b > a and b > c: my_max = "b"
# # if c > a: my_max = "c"
# # print(my_max)


# my_max = (a + b + abs(a - b))/2 #abs which mean តម្លៃដាច់ខាត
# print(my_max)



# m = int(input("Enter your score: "))
# p = int(input("Enter your score: "))
# c = int(input("Enter your score: "))
# average = (m + p + c) / 3
# if average >= 90 and average <= 100:      #if 100<= average >= 90
#     print("Grade A")
# elif average >= 80 and average < 90:      #if 90 < average >=80
#     print("Grade B")
# elif average >= 70 and average < 80:      #if 80 < average >= 70
#     print("Grade C")
# elif average >= 60 and average < 70:      #if 70 < average >= 60
#     print("Grade D")
# elif average >= 50 and average < 60:      #if 60 < average >= 50
#     print("Grade E")
# else:                                     #else:
#     print("Grade F")


# how to find the price of power that we use monthly
# total = int(input("Enter new month used: ")) - int(input("Enter old month used: "))
# if 0 < total <= 10:
#     payment = total * 450
# elif 10 < total <= 20:
#     payment = (10 * 450) + ((total- 10) * 550)
# elif 20 < total <= 30:
#     payment = (10 * 450) + (10 * 550) + ((total- 20) * 650)
# elif 30 < total <= 40:
#     payment = (10 * 450) + (10 * 550) + (10 * 650) + ((total- 30) * 750)
# else:
#     payment = (10 * 450) + (10 * 550) + (10 * 650) + (10 * 750) + ((total- 40) * 800)

# print(f"Payment = {payment} reil")





#Find year that have 29 in february
# year = int(input("Enter the year: "))
# if year % 400 == 0:
#     print(f"{year} is the leap year.")
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is the leap year.")
# else:
#     print(f"{year} is not the leap year.")



#Find the end day of the month
# month = input("Enter month: ").lower()
# year = int(input("Enter the year: "))
# if month == "january":
#     print(f'{month} ends at 31st')
# elif month == "february":
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         print(f"{month} ends at 29th")
#     else:
#         print(f"{month} ends at 28th")
# elif month == "march":
#     print(f"{month} ends at 31st")
# elif month == "april":
#     print(f"{month} ends at 30th")
# elif month == "may":
#     print(f"{month} ends at 31st")
# elif month == "june":
#     print(f"{month} ends at 30th")
# elif month == "july":
#     print(f"{month} ends at 31st")
# elif month == "august":
#     print(f"{month} ends at 31st")
# elif month == "septemper":
#     print(f"{month} ends at 30th")
# elif month == "october":
#     print(f"{month} ends at 31st")
# elif month == "november":
#     print(f"{month} ends at 30th")
# else:
#     print(f"{month} ends at 31st")



# correct_username = "Reaksa@gmail.com"
# correct_password = "good123"

# user_name = input("Enter your user name: ").strip() #strip which means not include space that users input unintentionally.
# password = input("Enter your password: ")

# if user_name == correct_username and password == correct_password:
#     print("Congratulation!")
# elif user_name == correct_username and password != correct_password:
#     print("Your password is invalid.")
# elif user_name != correct_username and password == correct_password:
#     print("Your username is invalid")
# else:
#     print("Your username and password are invalid.")




# temperature = float(input("Enter the temperature: "))
# unit = input("Do you want it to be (F)ahrenheit or (C)elsius?(F or C): ").upper().strip()
# if unit == "F":
#     result = (temperature * 9/5) + 32
#     print(f"{temperature}Celsius is {result} Fahrenheit")
# else:
#     result = (temperature - 32) * 5/9
#     print(f"{temperature}Fahrenheit is {result} Celsius")





# weight = float(input("Enter your weight : "))
# height = float(input("Enter your height: "))

# bmi = weight  / (height ** 2)
# if bmi <18.5:
#     print(f"Your BMW is {bmi:.2f}, you are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print(f"Your BMI is {bmi:.2f}, you are normal weight.")
# elif 24.9 <= bmi < 29.9:
#     print(f"Your BMI is {bmi:.2f}, you are overweight.")
# else:
#     print(f"Your BMI is {bmi:.2f}, you are obese.")


# import random
# correct_number = random.radiant(1, 100)
# correct_number = 56

# for i in range (1, 6):
#     guess = int(input("Enter your guess number: "))
#     if 0 < guess <= 40 :
#         print('Too low')
#     elif 60 < guess <= 100 :
#         print('Too high')
#     elif guess == 56:
#         print("Congratulations!!!")
#     else:
#         print("Almost correct, try again!")
#     i =+ 1




# light = input("Enter the traffic light: ")

# if light == "Red":
#     print("Stop!")
# elif light == "Yellow":
#     print("Should Stop!")
# elif light == "Green":
#     print("Go Ahead!")
# else:
#     print("It is not a traffic light.")






# balance = 100
# barcode = input("Enter your barcode: ")
# amount = float(input("How much do you want to withdraw?: "))

# if barcode == "Bobo123" and amount <= balance:
#     balance -= amount
#     print(f"Your withdraw money is ${amount} and your remaining money is ${balance}")
# elif barcode != "Bobo123" and amount <= balance:
#     print("Your barcode is invalid.") 
# elif barcode == "Bobo123" and amount >= balance:
#     print("Out of the balance.")
# else:
#     print("Your barcode and amount of money are invalide.")



# x = 11
# result = "Even" if x % 2 == 0 else "Odd"
# print(result)





# if .... else
# a = 20
# b = 10
# c = 30

# # my_max = a if b<a>c else b if a<b>c else
# my_max = "a" if b<a>c else "b" if a<b>c else "c"
# print(my_max)




# number = float(input("Enter number: "))

# result = "Postive Number" if number >= 0 else "Negative Number"
# print(result)



# number = float(input("Enter number: "))
# print(f"{number} is ", end="")
# print("Positive Number") if number >= 0 else print("Negative Number")


# a = "h" in "hello world"
# print(a)


# character = input("Enter a character: ").lower()
# result = "vowel" if character == "a" or character == "e" or character == "i" or character == "o" or character == "u" else "consanant"
# print(result)


# character = input("Enter a character: ").lower()
# result = "vowel" if character in "aeiou" else "consanant"
# print(result)



# character = input("Enter a character: ").lower()
# if len(character) == 1:
#     result = "vowel" if character in "aeiou" else "consanant"
#     print(f"{character} is {result}")
# else: 
#     print("Invalid Input")




# import random
# correct_num = random.randint(0, 10)
# guessing_num= int(input("Enter your guessing number: "))

# if guessing_num == correct_num:
#         print("Congratulation!!! You win the game. ")
# else:
#         print("Try Again!")
   



# import random
# correct_num = random.randint(0, 10)
# guessing_num= int(input("Enter your guessing number: "))

# print("Congratulation!!!") if guessing_num == correct_num else print("Try Again!")













