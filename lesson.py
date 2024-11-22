

#computing Angles by using thee following formula:
# A = acos((a * a - b * b - c * c) / (-2 * b * c))
# B = acos((b * b - a * a - c * c) / (-2 * a * c))
# A = acos((c * c - b * b - a * a) / (-2 * a * b))


# import math
# x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))
# a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
# b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
# c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

# A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
# B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
# C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
# print(f"The three angles are: {round(A * 100) / 100, round(B * 100) / 100, round(C * 100) / 100}")

# import random
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)
# answer = eval(input("What is " + str(number1) + " + " + str(number2) + '?'))
# print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

# original_price = 1000000
# good_credit = False
# if good_credit:
#     down_payment = 0.1 * original_price
# else:
#     down_payment = 0.2 * original_price
# print(f"Down payment: ${down_payment}")


# temperature = int(input("Enter the weather: "))

# if temperature > 30:
#     print("It is a hot day.")
# elif temperature < 10:
#     print("It is a cold day.")
# else:
#     print("It is neither hot nor cold.")


# temperature = 90
# if temperature > 30:
#     print("It is a hot day.")
# else: 
#     print("It is a cold day.")

# name = "Kyreadksfhlsdjfoiejdkfjieofdsklfjfmdsklfjkdjfskjslfjfiofjkdsfjiejfekfjdkncdjkfskdfjslfsjflsdkf"
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters.")
# else:
#     print("name looks good!")

# has_high_income = True
# good_credit = True
# if has_high_income and70
#  good_credit:
#     print("Eligibal for loan")


# weight = int(input("Enter your weight: "))
# unit = input("(L)bs or (k)g: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} k")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} L")

# score = int(input("Enter your score: "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"You got {grade}")

# x = 3
# y = 4
# if x < 2:
#     if y > 2:
#         z = x + y
#         print(f"Z is {z}")
#     else:
#         print(f"X is {x}")
# else:
#     print("I love u")


# a = True
# b = False

# result_or = a or b
# print(f"a or b: {result_or}")

# def positive_input(prompt):
#     while True:
#         value = int(input(prompt))
#         if value > 0:
#             return value
#         else:
#             print("Please enter a positive number")


# width = positive_input("Enter the width: ")
# height = positive_input("Enter the height: ")

# p = (width + height) * 2
# s = width * height
# print(f"Parameter of a rectangle is {p} m")
# print(f"Area of a rectangle is {s} m^2")def count_bits(n):
# def count_bits(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count
# n = int(input("Enter number: "))
# print(count_bits(n))
   




# def count_bits(n):
#     count = 0
#     while n:
#         count += n & 1  
#         n >>= 1         
#     return count

# n = int(input("Enter number: "))
# print(count_bits(n))


# def count_bits(n):
#     count = 0
#     while n:
#         count += n & 1 
#         n >>= 1         
#     return count

# n = int(input("Enter number: "))
# print(count_bits(n))

# person = {'name':" John", "age" : 30 , "city" : "New York"}
# for key, value in person.items():
#     print(f"{key}: {value}")

# name = {"Bopha" : "girl", "Dara": "boy", "Sophal": "girl"}
# for hounor, sex in name.items():
#     print(f"{hounor}: {sex}")



# print(" ||\n" * 50)
# print("|| " * 50)


#square
# s = float(input("Enter the number: "))
# P = 4 * s
# A = s ** 2
# print(f"Peremiter of Square = {P} cm")
# print(f"Area of Square = {A} cm^2")


# #rectangle
# l = float(input("Enter the length: "))
# w = float(input("Enter the weight: "))
# P = 2 * l + 2 * w
# A = l * w
# print(f"Perimeter of Rectangle = {P} cm")
# print(f"Area of Rectangle = {A} cm^2")



# #circle
# r = float(input("Enter the radius: "))
# pi = 3.14
# C = 2 * pi * r
# A = pi * r ** 2
# print(f"Perimeter of Circle = {C} cm")
# print(f"Area of Circle = {A} cm^2")

# #triangle
# a = 3
# b = 3
# c = 3
# h = 4
# P = a + b + C
# A = b * h / 2
# print(f"Perimeter of Triangle = {P} cm")
# print(f"Area of Triangle = {A} cm^2")

# #parallelogram
# a = 5
# b = 4
# h = 6
# P = 2 * a + 2 * b
# A = b * h
# print(f"Perimeter of Parallelogram = {P} cm")
# print(f"Area of Parallelogram = {A} cm^2")

# #circular sector
# pi = 3.14
# r = 3
# delta = 120
# L = pi * r * delta / 180
# A = pi * r ** 2 * L * delta / 360
# print(f"Length of the Arc = {L} cm")
# print(f"Area of a Segment of Circle = {A} cm^2")

#pythagorean theorem
# a = 2
# b = 3
# print(f" c^2 = {a ** 2 + b ** 2} cm")

#circular ring
# pi = 3.14
# R = 5
# r = 2
# A = pi * (R ** 2 - r ** 2)
# print(f"A = {A} cm^2")

#sphere
# pi = 3.14
# r = 2
# SA = 4 * pi * r ** 2
# V = 4 * pi * r ** 3 / 3
# print(f'V = {V} m^3')
# print(f"SA = {SA} m^2")



# count = 0
# while count <= 5:
#     print(count)
#     count += 1
# while True :
#     print("This will run forever unless stopped!")
#     break

# name = None
# while not(name):
#     name = input("Enter your name: ")
#     print("Hello " + name)
   
# number = 5
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"The factorial for {number} is {factorial}")


# value1 = 3
# value2 = 7
# value3 = 12

# min_value = 1
# max_value = 10
# values = [value1, value2, value3]
# i = 0

# while i < len(values):
#     value = values[i]
#     if min_value <= value <= max_value:
#         print(f"Value {value} is within the range.")
#     else :
#         print(f"Value {value} is out of range")
#     i +=1


# import time
# red = 10
# print("red")
# while red >= 1:
#     time.sleep(2)
#     print(red)
#     red -= 1
    
# print("\ngreen")
# green = 20
# while green >= 1:
#     time.sleep(2)
#     print(green)
#     green -= 1

# print("\norange")
# orange = 3
# while orange >= 1:
#     time.sleep(2)
#     print(orange)
#     orange -=1




# i = 5
# while i >= 1:
#     num = 1
#     for j in range (2, i - 1):
#         print(num, end = "H" )
#         num /= 2
#     print()
#     i -= 1
# 1H0.5H
# 1H

# n = 3
# for i in range(1, n + 1):
#     print(' ' * (n - i), end=" ")
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     for j in range(i - 1, 0, -1):
#         print(j, end=' ')
#     print()
#    1 
#   1 2 1
#  1 2 3 2 1


# count = 0
# while count < 100:
#     print("Program is fun!")
#     count = 1 + count


# sum = 0
# i = 1
# while i < 10:
#     sum = sum + i
#     i = i + 1
# print(f"sum is {sum}")


#Example 2
# import random
# number = random.randint(0, 100)
# print("Guess a magic number between 0 and 100")

# guess = -1
# while guess != number:
#     guess = eval(input("Enter your guess: "))
#     if guess == number:
#         print(f"Yes, the number is {number}")
#     elif guess > number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")

# Example1:
import random
# import time

# correctCount = 0
# count = 0
# number_of_questions = 5

# startTime = time.time()

# while count < number_of_questions:
#     number1 = random.randint(0 % 9)
#     number2 = random.randint(0 % 9)

#     if number1 < number2:
#         number1, number2 = number2, number1

#     answer = eval(input("What is" + str(number1) + "-" + str(number2) + "?"))

#     if number1 - number2 == answer:
#         print("You are correct!")
#         correctCount += 1
#     else:
#         print("Your answer is wrong.\n", number1, "-", number2, "is", number1 - number2)

#     count += 1
#     endTime = time.time()
#     testTime = int(endTime - startTime)
#     print("Correct count is", correctCount, "out of", number_of_questions, "\nTest time is", testTime, "seconds")


#Exercise
# data = eval(input("Enter an integer (the input ends)" + "if it is 0): "))
# sum = 0
# while data != 0:
#     sum += data
#     data = eval(input("Enter an integer (the input ends)" + "if it is 0): "))
# print(f"The sume is {sum}")


# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1
    
# number = eval(input("Enter an interger: "))
# max = number
# while number != 0:
#     number = eval(input("Enter an interger: "))
#     if number > max:
#         max = number
# print(f"max is {max}")
# print(f"number is {number}")




# number = 0
# sum = 0
# for count in range(5):
#     number = eval(input("Enter an integer: "))
#     sum += number
# print(f"sume is {sum}")
# print(f"count is {count}")

#convert while to for
# sum = 0                 sum = 0
# i = 1                   for i in range(1001):
# while i < 1001:             sum += 1
#     sum += i
#     i += 1



#loops nested
# print("         Multiplication Table")
# print(" |", end = "")
# for j in range(1, 10):
#     print(" ", j, end = "")
# print()
# print("-----------------------------------------")

# for i in range(1, 10):
#     print(i, "|", end = '')
#     for j in range(1, 10):
#         print(format(i * j, "4d"), end = "")
# print()

# for i in range(1, 5):
#     j = 0
#     while j < i:
#         print(j, end = " ")
#         j += 1
# #output
# # 0 0 1 0 1 2 0 1 2 3


# i = 0
# while i < 5:
#     for j in range(i, 1, -1):
#         print(j, end = " ")
#     print("****")
#     i += 1
# #output
# # ****
# # ****
# # 2 ****
# # 3 2 ****
# # 4 3 2 ****    


# i = 5
# while i >= 1:
#     num = 1
#     for j in range(1, i + 1):
#         print(num, end = "xxx")
#         num *= 2
#     print()
#     i -= 1
# # 1xxx2xxx4xxx8xxx16xxx
# # 1xxx2xxx4xxx8xxx
# # 1xxx2xxx4xxx
# # 1xxx2xxx
# # 1xxx

# i = 1
# while i <= 5:
#     num = 1
#     for j in range(1, i + 1):
#         print(num, end = "G")
#         num += 2
#     print()
#     i += 1
# # 1G
# # 1G3G
# # 1G3G5G
# # 1G3G5G7G
# # 1G3G5G7G9G



# 5.5 Minimiing Numerical errors
# sum = 0
# i = 0.01
# while i <= 1.0:
#     sum += i
#     i = i + 0.01
# print(f"The sum is {sum}")

# sum = 0
# count = 0
# i = 0.01
# while count < 100:
#     sum += i
#     i = i + 0.01
#     count += 1
# print(f"The sum is {sum}")


# sum = 0
# i = 0.01
# for count in range(100):
#     sum += i
#     i = i + 0.01
# print(f'The sum is {sum}')

# both outputs are the same 50.5



# Greatest common divisor
# n1 = eval(input("Enter first integer: "))
# n2 = eval(input("Enter second integer: "))
# gcd = 1
# k = 2
# while k <= n1 and k <= n2:
#     if n1 % k == 0 and n2 % k == 0:
#         gcd = k
#     k += 1
# print(f"The greatest common divisor for {n1} and {n2} is {gcd}")

# Enter first integer: 125
# Enter second integer: 2525
# The greatest common divisor for 125 and 2525 is 25


# sum = 0
# number = 0
# while number < 20:
#     number += 1
#     sum += number
#     if sum >= 100:
#         break
# print(f"The number is {number}")
# print(f"The sum is {sum}")




# balance = 1000
# while True:
#     if balance < 9:
#         break
#     balance = balance - 9
# print(f"Balance is {balance}")


# balance = 1000
# while True:
#     if balance < 9:
#         continue
#     balance = balance - 9
# print(f"Balance is {balance}")


# for i in range(1, 4):
#     for j in range(1, 4):
#         if i * j == 2:
#            continue
#         print(i * j)
    
#     print(i)



# year = 0
# tuition = 1000
# while tuition < 20000:
#     year += 1
#     tuition = tuition * 1.07
# print(f"Tuition will be doubled in {year} years")
# print(f"Tuition will be $ {tuition:.2f} in {year} years")


# Tuition will be doubled in 45 years
# Tuition will be $ 21002.45 in 45 years

# n = 3
# factor = 2
# while factor <= n:
#     if n % factor == 0:
#         break
#     factor += 1
# print(f'The smallest factor other than 1 for {n} is {factor}')
# The smallest factor other than 1 for 3 is 3

#incorrect 
# i = 0
# while i < 4:
#     if i % 3 == 0:
#         continue
#     sum += i
#     i += 1

#correct
# i = 0                                                             
# while i < 4:
#     if i % 3 == 0:
#         i += 1  # Increment `i` before continuing
#         continue
#     sum += i
#     i += 1



# kg = 1
# pound = 20

# print("Kilograms   Pounds   |   Pounds   Kilograms")
# while kg <= 10 and pound <= 50:
#     pounds = kg * 2.2  
#     kilograms = pound * 0.45  
    
#     print(f"{kg:<10} {pounds:<8.2f} |   {pound:<7} {kilograms:.2f}") #accurate formatted printing
    
#     kg += 2 #change "kg +2" to the right increment format, which is "kg += 2"
#     pound += 5  


# kg = 1  # Start with 1 kilogram
# pound = 20  # Start with 20 pounds

# # Print table headers
# print("Kilograms    Pounds   |   Pounds   Kilograms")

# # Loop through both kg and pound conversion tables
# while kg <= 10 and pound <= 50:  # Can be 'or' depending on your goal
#     pounds = kg * 2.2  # Convert kg to pounds
#     kilograms = pound * 0.45  # Convert pounds to kilograms

#     # Properly formatted printing for clear table-like output
#     print(f"{kg:<10} {pounds:<8.2f} |   {pound:<7} {kilograms:.2f}")

#     # Increment kg by 2 and pound by 5 for next loop iteration
#     kg += 2
#     pound += 5


# count_positive = 0
# count_negative = 0
# total = 0
# count = 0

# while True:
#     num = int(input("Enter an integer, the input ends if it is 0: "))
    
#     if num == 0: # add "= "since "num = 0: " is not accurate. 
#         break
    
#     if num > 0:
#         count_positive += 1
#     elif num < 0:
#         count_negative += 1
    
#     total += num
#     count += 1

# average = total / count
# print("Positive numbers:", count_positive)
# print("Negative numbers:", count_negative)
# print("Total:", total)
# print("Average:", average)  



# kg = 1

# while kg <= 20:
#     pounds = kg * 2.2  
#     print(kg, "     ", pounds)
#     kg += 2 #change "kg +2" to the right one which is "kg += 2". 




# tuition = 10000
# year = 1

# while year <= 10:
#     tuition += tuition * 0.05 
#     year += 1  # change "year +1" to "year += 1 which is a right increment"

# print("Tuition in 10 years:", tuition)

# total_cost = 0
# for i in range(4):
#     total_cost += tuition

# print("Total cost for four years' tuition after 10 years:", total_cost)












