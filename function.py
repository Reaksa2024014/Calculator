

# def max(num1, num2):
#     if num1 > num2:
#         result = num1
#     else:
#         result = num2
#     return result

# def main():
#     i = 5
#     j = 2
#     k = max(i, j)
#     print(f"The larger number of {i} and {j} is {k}")

# main()




#without return value
# def Grade(score):
#     if  100 >= score >= 90:
#         print("A")
#     elif 90 > score >= 80:
#         print("B")
#     elif 80 > score >= 70:
#         print("C")
#     elif 70 > score >= 60:
#         print("D")
#     else:
#         print("F")
# def main():
#     score = eval(input("Enter a score: "))
#     print("The grade is" , end= " ")
#     Grade(score)
# main()


#with return function
# def Grade(score):
#     if  100 >= score >= 90:
#         return "A"
#     elif 90 > score >= 80:
#         return "B"
#     elif 80 > score >= 70:
#         return "C"
#     elif 70 > score >= 60:
#         return "D"
#     else:
#         return "E"
# def main():
#     score = eval(input("Enter a score: "))
#     print("The grade is" , Grade(score))
    
# main()






# def sum(num1, num2):
#     total = num1 + num2
#     return total
# print(sum(1, 2))



# def function(n, m):
#     result = function2(n)
#     return result

# def function2(n):

#     if n > 0:
#         return 1
#     elif n == 0:
#         return 0
#     elif n < 0:
#         return -1
    
# output = function(2, 3)
# print(output)








# def function_name():
#     statements



# def greeting():
#     print("Hello, how is it going.. ")
# greeting()



# def add():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x + y
#     print(f"{x} + {y} = {result}")
# # add()



# def sub():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     z = int(input("Enter z: "))

#     result = x - y - z
#     print(f"{x} - {y} - {z} = {result}")
# # sub()


# def multiplication():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x * y
#     print(f"{x} * {y} = {result}")
# # multiplication()


# def division():
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x / y
#     print(f"{x} / {y} = {result}")
# # division()


# def moldulus():
    
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x % y
#     print(f"{x} % {y} = {result}")
# # moldulus()


# def floor_division():
    
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x // y
#     print(f"{x} // {y} = {result}")
# # floor_division()


# def exponential():
    
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
    
#     result = x ** y
#     print(f"{x} ** {y} = {result}")
# # exponential()

# def menu():
#     print("""
          
#             1. Add
#             2. Substraction
#             3. Multiplication
#             4. Division
#             5. Moldulus
#             6. Floor Division
#             7. Exponentation         
#     """ )






# # def calculation():
# #     menu()
# #     choice = input("Please choose one operation: ")

# #     while True:
# #         if choice == '1':
# #             add()
# #         elif choice == "2":
# #             sub()
# #         elif choice == "3":
# #             multiplication()
# #         elif choice == "4":
# #             division()
# #         elif choice == "5":
# #             moldulus()
# #         elif choice == '6':
# #             floor_division()
# #         elif choice == "7":
# #             exponential()
# #         else:
# #             print("Invalid input. Try again!!!")

# # calculation()




# import os
# def calculation():
    
    
#     while True:
#         menu()
#         choice = input("Please choose one operation: ")
#         if choice == '1':
#             add()
#         elif choice == "2":
#             sub()
#         elif choice == "3":
#             multiplication()
#         elif choice == "4":
#             division()
#         elif choice == "5":
#             moldulus()
#         elif choice == '6':
#             floor_division()
#         elif choice == "7":
#             exponential()
#         else:
#             print("Invalid input. Try again!!!")

#         key = input("Do you want to calculate again?[yes/no]: ").lower()
#         if key == 'no':
#             break
#         os.system('cls')

# calculation()







# def add() -> None:
#     print('Hollo world')
#     return
# add()


# def message() -> str:
#     return"Hello, nice to meet u"
# print(message())


# def message() -> None:
#     return None
# print(message())

     
# def getMessage():
#     message = input('Enter your message: ')
#     return message
# # mss = getMessage()
# # print(mss) or 
# print(getMessage())


# def getVoter() -> str:
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         return "You can vote."
#     else:
#         return"You can not vote."
    
# print(getVoter())







# def factorail() -> int:
#     n = int(input('Enter n: '))
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#         i += 1
#     return result
# print(factorail()+factorail())



# def my_sum() -> int:
#     n = int(input("Enter n: "))
#     sum = 0
#     for i in range (1, n+1):
#         sum += i
#         i+= 1
#     return sum
# print(my_sum())    


# def my_max() -> int:
#     a = int(input('Enter a: '))
#     b = int(input("Enter b: "))
#     if a > b:
#         return a
#     else:
#         return b
# print(my_max())


# def my_min() -> int:
#     a, b = int(input('Enter a: ')), int(input("Enter b: "))
#     if a < b:
#         return a 
#     else:
#         return b 
# print(my_min())


# def my_max() -> int:
#     a = int(input('Enter a: '))
#     b = int(input("Enter b: "))
#     if a > b: return a
#     else: return b
# print(my_max())



# def factorail() -> int:
#     """
#         reference: https://chatgpt.com/c/671e06a3-99f0-8007-85ff-cd6ede437b88

#     """
#     n = int(input('Enter n: '))
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#         i += 1
#     return result


# factorail()


# def max(num1, num2):
    
#     if num1 > num2:
#         result = num1
#     else:
#         result = num2
#     return result
# print(max(7, 5))




# def add(a, b) -> int:
#     result = a + b
#     return result

# result = add(10, 20)
# print(result)


# def find_grade(avg) -> float:
#     grade = None
#     if 100 >= avg >= 90:
#         grade = "A"
#     elif avg >= 80:
#         grade = "B"
#     elif avg >= 70:
#         grade = "C"
#     elif avg >= 60:
#         grade = "D"
#     elif avg >= 50:
#         grade = "E"
#     else:
#         grade = "F"
#     return grade
# average = float(input("Enter average: "))
# print(find_grade(average))





# def find_total(sc1, sc2, sc3):
    
#     total = sc1 + sc2 + sc3
#     return total
# result = find_total(10, 20, 30)
# print(result)






# def find_total(sc1, sc2, sc3):
    
#     sc1 = float(input('Enter score1: '))
#     sc2 = float(input('Enter score2: '))
#     sc3 = float(input('Enter score3: '))
#     total = sc1 + sc2 + sc3
#     return total
    
# result = find_total("sc1", "sc2", "sc3")
# print(result)




# # def find_average( ):
# #     average = result / 3
# #     return average
# # print(find_average)


# def find_average(total, sub):
#     average = total / sub
#     return average
# print(find_average(result, 3))


# def find_grade(avg) -> float:
#     grade = None
#     if 100 >= avg >= 90:
#         grade = "A"
#     elif avg >= 80:
#         grade = "B"
#     elif avg >= 70:
#         grade = "C"
#     elif avg >= 60:
#         grade = "D"
#     elif avg >= 50:
#         grade = "E"
#     else:
#         grade = "F"
#     return grade

# print(find_grade(find_average(result, 3)))



# x = 400
# def func1() -> None:
#     global x 
#     x = 600
#     print(f"x inside function1 = {x}")

# func1()
# print(f"x outside function1 = {x}")
# print(f"x outside function1 = {x}")
# print(f"x outside function1 = {x}")





# def container():
#     def add(a, b):
#         print(a + b)
#     add(40, 50)
# container()


# def container():
#     def add(a, b):
#         print(a + b)

#     def sub(a, b):
#         print(a - b)
#     return add, sub

# a = container()[0]
# a(70,30)


# def container():
#     def add(a, b):
#         print(a + b)
#         return "hello"

#     def sub(a, b):
#         print(a - b)
#         return 123 

#     return [add, sub]

# a = container()
# # print(a[1](60, 70))
# # a(70,30)
# i = 0
# while i<len(a):
#     a[i](10, 30)
#     i += 1


# def mul(a, b):
#     return a * b
# m = mul
# print(m(10, 4))









# def add_numbers(a, b):
#     return  a + b 
# a,b = eval(input("Enter a: ")), eval(input("Enter b: "))
# print(add_numbers(a,b))


# def is_even(num):
#     return num % 2 == 0
# print(is_even(4))


# def factorial(n):
#     n = abs(n)
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(factorial(5))
# print(factorial(7))


# def find_max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c: 
#         return b
#     else:
#         return c
# print(find_max(50, 40, 30))


# def my_max(a, b, c):
#     return a if b<a>c else b if a<b>c else c
# print(my_max(50, 60, 70))


# def is_even(a):
#     return a % 2 == 0
# print(is_even(int(input("Enter the number: "))))




# function_name = lambda params: expression
# leap_year = lambda year: year % 400 == 0 or year % 4 == 0 and year % 100 != 0
# print(leap_year(2024))


# even_num = lambda number: number % 2 == 0
# print(even_num(5))