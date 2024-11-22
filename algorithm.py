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


# Algorithm of reverse number
# 1. start
# 2. input num
# 3. define reverse = 0, remain
# 4. while num > 0:  // num = 123
#    remain = num % 10  // reverse = 321
#    reverse = reverse * 10 + remain
#    num = num // 10





a = 0
b = 1
next = 0
n = int(input("Ënter n: "))
print(a, b)
for i in range (n):
    next = a + b
    print(next)
    a = b
    b = next



