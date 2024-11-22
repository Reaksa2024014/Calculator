# my_list = list([1, 2, 3, 4])
# print(my_list)
# print(type(list))

# print(my_list[3])

# my_list[2] = 50
# print(my_list)





# fruites = ["apple", "mango", "hello", "banana", "wood apple", 1, 3, 53, 7, 5j, "beautiful", True, False]
# i = 0
# l = len(fruites)
# while i < l:
#     print(f"fruite[{i}]:", fruites[i])
#     i +=1

# print(fruites[::-1])   #reverse items
# print(fruites[-1])



# i = -1
# l = len(fruites)
# while i >= -l:
#     print(fruites[i])
#     i-=1



# l = len(fruites)
# i  = 1
# while i <= l:
#     print(fruites[-i])
#     i += 1

# l = len(fruites)
# i = l - 1
# while i >= 0:
#     print(fruites[i])
#     i-=1


# search = "banana"
# l = len(fruites)
# i = 0
# while i <l:
#     if search == fruites[i]:
#         print(f'{search} is found in fruites.')
#         break
#     i += 1


class_a = ["seng hour", "menghong", "lyna", "sreynith", "nita", "vitou", "meng"]
name = input("Enter the name: ")
l = len(class_a)
i = 0
isFound = False  #instance variable
while i < l:
    if name == class_a[i]:
        print(f"{name} is found in class.")
        isFound = True
        break
    i += 1
if not isFound:
    print("Not found.")