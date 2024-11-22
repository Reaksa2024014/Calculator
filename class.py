# class MyClass:
#     def __init__(self, value):
#         self.value = value  # 'self.value' is an instance attribute

#     def print_value(self):
#         print(self.value)  # Accessing the instance's value attribute

# # Creating an instance of MyClass
# obj = MyClass(10)
# obj.print_value()  # Outputs: 10



# class Dog:
#     def __init__(self, name):  # Use double underscores: __init__
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says: Woof!")

# # Creating an instance of Dog
# my_dog = Dog("Buddy")

# # Calling the bark method
# my_dog.bark() 


# class Book:
#     def __init__(self, title: str, author: str, ISBNNum: str):
#         self.__title = title
#         self.__author = author
#         self.__ISBNNum = ISBNNum
#         self.__is_available = True  # Private attribute indicating availability

#     def check_availability(self) -> bool:
#         return self.__is_available

#     def set_availability(self, availability: bool) -> None:
#         self.__is_available = availability


# class Users:
#     def __init__(self, name: str, member_id: int):
#         self.__name = name
#         self.__member_id = member_id

#     def borrow_book(self, book: Book) -> bool:
#         if book.check_availability():
#             book.set_availability(False)
#             return True
#         else:
#             return False

#     def return_book(self, book: Book) -> None:
#         book.set_availability(True)


# class Printer:
#     def _init_(self, text):
#         self_message = text
#     def print_message(self):
#         print(self.message)

# class NewsPrinter(Printer):
#     def print_message(self):
#         print(f"News:(self.message)")
# news = NewsPrinter("Hello World")


# text = "hello"
# print("Length of text:", len(text))
# print("Smallest character:", min(text))
# print("Largest character:", max(text))


# #Task1
# # Get user input
# user = input("Enter a sentence: ")
# min_char = min(user)
# max_char = max(user)

# # Display length and ASCII values of characters
# print(f"Length of the sentence: {len(user)}")
# print(f"The smallest ASCII value: {ord(min_char)}")
# print(f"The largest ASCII value: {ord(max_char)}")

# # Initialize attempts for the overall guessing process
# attempts = 1
# max_attempts = 3

# # Main guessing loop
# while attempts <= max_attempts:
#     guess1 = input("Guess the smallest character: ")
#     guess2 = input("Guess the largest character: ")

#     if guess1 == min_char and guess2 == max_char:
#         print("Congratulations!!! Your guesses are correct.")
#         break
#     elif guess1 != min_char and guess2 == max_char:
#         print("Incorrect smallest character. Try again!!!")
#         sub_attempts = 1
#         while sub_attempts < max_attempts:  # Changed to < max_attempts to allow 3 tries
#             guess1 = input("Guess the smallest character again: ")
#             if guess1 == min_char:
#                 print("Correct smallest character.")
#                 break
#             else:
#                 print("Still incorrect.")
#             sub_attempts += 1
#         if sub_attempts == max_attempts:
#             print("You've reached the maximum attempts for the smallest character.")
#             break
#     elif guess1 == min_char and guess2 != max_char:
#         print("Incorrect largest character. Try again!!!")
#         sub_attempts = 1
#         while sub_attempts < max_attempts:  # Changed to < max_attempts to allow 3 tries
#             guess2 = input("Guess the largest character again: ")
#             if guess2 == max_char:
#                 print("Correct largest character.")
#                 break
#             else:
#                 print("Still incorrect.")
#             sub_attempts += 1
#         if sub_attempts == max_attempts:
#             print("You've reached the maximum attempts for the largest character.")
#             break
#     else:
#         print("Both characters are incorrect. Try again!!!")
    
#     attempts += 1

# if attempts > max_attempts:
#     print("You reached the maximum attempts.")



# #Task2
# # Create a string of at least 8 characters
# text = "abcdefgh"  # Example string

# # Display the first, middle, and last character
# first_character = text[0]
# middle_index = len(text) // 2  # Calculate the middle index
# middle_character = text[middle_index]
# last_character = text[-1]

# print(f"First character: {first_character}")
# print(f"Middle character: {middle_character}")
# print(f"Last character: {last_character}")

# # Print every second character in the string
# print("Every second character:")
# for i in range(len(text)):
#     if i % 2 == 1:  # Check if index is odd
#         print(text[i], end=' ')
# print()  # For a new line after printing

# # Swap the first and last characters
# if len(text) > 1:  # Check if string length is more than 1 to avoid errors
#     swapped_text = last_character + text[1:-1] + first_character
# else:
#     swapped_text = text  # If the string is of length 1, it remains the same

# print(f"Updated string after swapping first and last characters: {swapped_text}")



# #task3
# # A. Create a sentence
# sentence = "This is an example sentence for task three."

# # Slice the first half and second half separately
# half_index = len(sentence) // 2  # Calculate the middle index
# first_half = sentence[:half_index]
# second_half = sentence[half_index:]

# print("First half:", first_half)
# print("Second half:", second_half)

# # B. Reverse the entire sentence using slicing
# reversed_sentence = sentence[::-1]
# print("Reversed sentence:", reversed_sentence)

# # C. Print the middle three characters if the string has an odd number of characters
# if len(sentence) % 2 == 1:  # Check if the length is odd
#     middle_index = len(sentence) // 2  # Middle index for odd length
#     middle_three = sentence[middle_index - 1:middle_index + 2]  # Get middle three characters
#     print("Middle three characters:", middle_three)


# #task4
# # Personalize the greeting and name
# greeting = "Hello"
# name = "YourName"  # Replace with your actual name

# # Print the personalized greeting
# personalized_greeting = greeting + ", " + name + "!"
# print("Personalized Greeting:", personalized_greeting)

# # Create Patterns
# pattern1 = (greeting + " ") * 3 + name + " " + (greeting + " ") * 2
# print("Pattern 1:", pattern1)

# # Calculate and print the total length of Pattern 1
# length_pattern1 = len(pattern1)
# print("Total length of Pattern 1:", length_pattern1)

# # Create another interesting pattern
# pattern2 = (greeting + " ") * 2 + name + " " + (greeting + " ") * 4 + name
# print("Pattern 2:", pattern2)

# # Calculate and print the total length of Pattern 2
# length_pattern2 = len(pattern2)
# print("Total length of Pattern 2:", length_pattern2)



#task5
# Create a sentence
# sentence = "Python is a great programming language."

# # Prompt the user to enter a word
# user_word = input("Enter a word: ")

# # Check if the word is not in the sentence
# if user_word not in sentence:
#     # Suggest adding it to the end and display the updated sentence
#     updated_sentence = sentence + " " + user_word
#     print(f"The word '{user_word}' is not in the sentence. Suggested update: {updated_sentence}")
# else:
#     # If the word is in the sentence, find and print the position of the word
#     position = sentence.index(user_word)  # Get the position of the word
#     print(f"The word '{user_word}' is found at position: {position}")



# #task6
# # 1. Create two strings
# string1 = "apple"
# string2 = "banana"

# # 2. Compare the strings
# if string1 == string2:
#     print("Both strings are equal.")
# else:
#     # 3. Determine which string comes first alphabetically
#     if string1 < string2:
#         print(f"{string1} comes before {string2}.")
#     else:
#         print(f"{string2} comes before {string1}.")

# # If the strings are identical in position
# if string1 == string2:
#     print("The strings are identical in position.")

# # Iterating Through Characters in a String
# print("\nCharacters in string1:")
# for char in string1:
#     print(char)



# import random
# nums = [5, 3, 4, 1, "AUPP", True, False]
# print(len(nums))
# print(min(nums))
# print(min(nums))
# print(max(nums))
# random.shuffle(nums)
# print(nums)


# squares = [x**2 for x in range(5)]

# print(squares) 


# names = ["Alice", "Bob", "Charlie"]

# for name in names:

#     print(name)

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# print(list1 == list2) 


# items = [3, 1, 2]
# items.append(4)
# items.sort()
# print(items)


# # Prompt the user to enter a series of integers
# user_input = input("Enter at least 10 numbers, separated by spaces: ")

# # Convert the input string into a list of integers
# numbers = [int(num) for num in user_input.split()]

# # Check if there are at least 10 numbers
# if len(numbers) < 10:
#     print("Error: You must enter at least 10 numbers.")
# else:
#     # Display the list of numbers entered
#     print("Numbers:", numbers)
    
#     # Calculate and display the maximum, minimum, sum, and average
#     max_num = max(numbers)
#     min_num = min(numbers)
#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
    
#     print(f"Max: {max_num}, Min: {min_num}, Sum: {total_sum}, Average: {average:.2f}")




# # Prompt the user to enter a series of integers
# user_input = input("Enter at least 10 numbers, separated by spaces: ")

# # Convert the input string into a list of integers
# numbers = [int(num) for num in user_input.split()]

# # Check if there are at least 10 numbers
# if len(numbers) < 10:
#     print("Error: You must enter at least 10 numbers.")
# else:
#     # Ask the user for the index and value to insert
#     index, value = map(int, input("Enter index and value to insert: ").split())
    
#     # Insert the value at the specified index in the numbers list
#     numbers.insert(index, value)
#     print("Updated list:", numbers)
    
#     # Remove the smallest number from the list
#     numbers.remove(min(numbers))
#     print("After removing the smallest element:", numbers)

# numbers = [3, 6, 2, 9, 5, 7, 1, 8]
# # Get index and value from the user
# index = int(input("Enter index: "))
# value = int(input("Enter value: "))

# # Insert value at the specified index
# numbers.insert(index, value)

# # Remove the smallest number
# numbers.remove(min(numbers))

# print("Updated list:", numbers)


# Prompt the user to enter a series of integers
# user_input = input("Enter at least 10 numbers, separated by spaces: ")

# # Convert the input string into a list of integers
# numbers = [int(num) for num in user_input.split()]

# # Check if there are at least 10 numbers
# if len(numbers) < 10:
#     print("Error: You must enter at least 10 numbers.")
# else:
#     # Ask the user for the index and value to insert
#     index, value = map(int, input("Enter index and value to insert: ").split())
    
#     # Insert the value at the specified index in the numbers list
#     numbers.insert(index, value)
#     print("Updated list:", numbers)
    
#     # Remove the smallest number from the list
#     smallest_number = min(numbers)
#     numbers.remove(smallest_number)
    
#     # Display the updated list after removing the smallest number
#     print("After removing the smallest element:", numbers)


# # Prompt the user to enter a series of integers
# numbers_input = input("Enter numbers (at least 10, separated by spaces): ")

# # Split the input string into a list of integers
# numbers = [int(num) for num in numbers_input.split()]

# # Calculate the maximum, minimum, sum, and average
# max_num = max(numbers)
# min_num = min(numbers)
# total_sum = sum(numbers)
# average = total_sum / len(numbers)

# # Display the results
# print("Numbers:", numbers)
# print("Max:", max_num, ", Min:", min_num)
# print("Sum:", total_sum, ", Average:", average)