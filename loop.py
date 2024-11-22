


# for i in range(1):
#     print("*", end="")
# print()


# for i in range(2):
#     print("*", end="")
# print()


# for i in range(3):
#     print("*", end="")
# print()


# for i in range(4):
#     print("*", end="")
# print()


# for i in range(5):
#     print("*", end="")
# print()


# for i in range (5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()



# for i in range (4):
#     for j in range(5):
#          print("*", end=" ")
#     print()


# for i in range(1):
#     print(i+1, end="")
# print()

# for i in range(2):
#     print(i+1, end=" ")
# print()

# for i in range(3):
#     print(i+1, end=" ")
# print()


# for i in range(1, 4):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()




# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(i):
#         print("*", end= " ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print("*", end= " ")
#     print()

# for i in range(5):
#     print("* "*(i+1))


# for j in range(5):
#     print("*", end=" ")
# print()

# for j in range(4):
#     print("*", end=" ")
# print()

# for j in range(3):
#     print("*", end=" ")
# print()

# for j in range(2):
#     print("*", end=" ")
# print()

# for j in range(1):
#     print("*", end=" ")
# print()



# n = 8
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()


# for i in range(5):
#     for j in range(5-i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     print("* "* i )





# for i in range (5):
#     print("  "*(4-i), end="")
#     print("* "*(i +1))



# for j in range(4):
#     print("  ", end="")
# for j in range(1):
#     print("*", end="")
# print()



# for i in range (5):
#     for j in range(5-(i+1)):
#         print("  ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()



# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or i == n - 1:
#             print("*", end=" ")
#         else:
#             print("  ", end="")
#     print(f"       i =  {i}")



# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or i == n - 1:
#             print(j, end=" ")
#         else:
#             print("  ", end="")
#     # print(f"       i =  {i}")
#     print()



# while condition:
#     statements

# i = 0
# while i < 2:
#     print("Python is fun!")
#     i +=1

# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#     i +=1

# import time
# import os

# while True:
#     print("red light!")
#     time.sleep(5)
#     os.system("cls") #for clear screen

#     print("green light!")
#     time.sleep(5)
#     os.system("cls")

#     print("yellow light!")
#     time.sleep(3)
#     os.system("cls")




# answer = None
# while answer != "yes":
#     answer = input("do you hate me(yes/no)? : ").lower()
# print(answer)





# answer = "yes"
# answer = input("do you love me(yes/no)? : ").lower()

# while answer != "yes":
#     print(answer)



# import time
# import os 

# seconds = 55
# while True:
#     if seconds == 60:
#         seconds = 0
#     print(seconds)
#     time.sleep(1)

#     os.system("cls")
#     seconds+=1






# import time
# import os

# seconds = 55
# minutes = 59
# hour = 23
# day = 0


# while True:
#     if seconds == 60:
#         minutes += 1
#         if minutes == 60:
#             hour +=1
#             if hour == 24:
#                 day+= 1
#                 hour = 0
#             minutes = 0
#         seconds = 0
#     print(" "*30, f"{day}:{hour}:{minutes}:{seconds}")
#     time.sleep(1)
#     os.system("cls")
#     seconds+=1









# break
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print("step", i)
#     i += 1



# answer = None
# print("Can you be my girlfriend?")
# while True:
#     answer = input("[yes/no]: ")
#     if answer == "yes" or answer == "no":
#         break
# print("end loop! your answer is ", answer)



# correct_password = "@123"
# while True:
#     answer = input("Enter your password: ")
#     if answer == correct_password:
#         break
#     else:
#         print("Incorrect password!")
# print("Log in successfully.")


    
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)




# for i in range(1, 101):
#     if 50<= i <= 60:  # if i >= 50 and i <= 60 # if i in range(50, 61)
#         continue
#     print(i)



# for i in range(1, 101):
#     if i % 2 == 0:
#          continue
#     print(i)


# for i in range(1, 101):
#     if i % 2 != 0:  # if i % 2 > 0 # if i % 2 == 1
#         continue
#     print(i)


# Algorithm of guessing number
# 1. start
# 2. s = 1, e = 100, correct = random
# 3. guess
# 4. while True:
#     if guess == correct:
#         then Congratulation!! you won.WindowsError
#         break
#     else:
#         if guess < correct:
#             s = guess
#             help = ciel((s + 100) / 2)
#         else:
#             e = guess
#             help = ciel((s + e) / 2)



# n = int(input("Enter n: "))
# result = 1
# i = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)


# n = int(input('Enter n: '))
# factorial = 1
# i = 1
# for i in range(1, n+1):
#     factorial *= i
#     i += 1
# print(factorial)
