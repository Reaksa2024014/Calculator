# number = eval(input("Enter an integer: "))
# max = number
# while number != 0:
#     number = eval(input("Enter an integer: "))
#     if number > max:
#         max = number
# print("max is", max)
# print("number", number)




# count = 0
# while count < 100:
#     #   Point A
#        print("Programming is fun!")
#        count += 1
#       # Point B
# # Point C


# i = 1 
# while i < 10:
#     if i % 2 == 0:
#         print(i)



# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#         i +=1

# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1



# number = 0
# sum = 0
# for count in range(5):
#      number = eval(input("Enter an integer: "))
#      sum += number
# print("sum is", sum)
# print("count is", count)



# sum = 0
# for i in range(100):
#     sum = sum + i
    
    

# i = 0
# sum = 0
# while i < 100:
#     sum += i
#     i += 1
#    


# i = 1
# sum = 0
# while sum < 10000:
#     sum = sum + i
#     i += 1


# i = 1
# for sum in range(10000):
#     i += 1



# x = input("Enter a character: ")
 # ch = chr(ord(x) + 3)
# print(ch)

# x = input("Enter a character: ")
# y = input("Enter a character: ")
# print(ord(y) - ord(x))







# print(format(5789.467657, "9.3f"))
# print(format(5789.467657, "<9.3f"))
# print(format(5789.4, ".2f"))
# print(format(5789.4, "<.2f"))
# print(format(5789.4, ">9.2f"))




# def count_char(s,char):
#     count = 0
#     for c in s:
#         if c == char:
#             count += 1
#     return count
# print(count_char("banana", "a"))


# import math
# angel_degrees = (math.pi/ 7) * (180 / math.pi)


# def add_numbers(a, b):
#     return a + b
# print(add_numbers(10, 20))



# i = 1
# sum = 0

# while sum < 10000:
#     sum = sum + i
#     i += 1



# sum = 0

# for i in range(1, 100000):  # Use a large enough number to ensure the loop runs long enough
#     sum = sum + i
#     if sum >= 10000:
#         break    


# Midterm exam
# i = 1
# while i <= 5-3:
#     num = 1
#     for k in range(1, i + 1):
#         print(num, end="F")
#         num += 3
#     print()
#     i += 1



# for i in range(1, 4):
#     for j in range(1, 4):
#         if i * j > 2:
#             continue
#         print(i * j)
#     print(i)



# outer = 2
# inner = 3
# count = 0
# while outer > 0:
#     while inner > 0:
#         count += 1
#         inner -= 1
#         if count % 3 == 0:
#             break
#     outer -= 1
# print(inner, "  ", outer, "  ", count)



# for i in range(2, 4):
#     j = i - 1
#     while j >= 0:
#         if j % 2 == 0 or i % 2 != 0:
#             print(j, end= " ")
#         j -= 1
#     print()




# def testMe (a, b, *, c, d):
#     return sum([a, b, c, d])
# print(testMe(1, 2, c=3, d=4))





# Fix the String Reversal function
def reverse_string(s):
    reversed = ""
    for i in range(len(s) -1, -1, -1):
        reversed += s[i]
    return reversed
print(reverse_string("Python")) #Expected output: "nohtyP"



# def check_number(num):
#     if num > 0:
#         return"Positive"
#     elif num < 0:
#         return"Negative"
#     else:
#         return"Zero"
# print(check_number(-5))
# print(check_number(0))
# print(check_number(10))



# counter = 0
# def increment():
#     global counter
#     counter += 1
#     return counter

# print(increment())
# print(increment())

# output
# 1
# 2