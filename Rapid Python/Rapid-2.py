# String Manipulation in Python
# text="Hello My World!"

# # Removes whitespace from both ends
# text = text.strip()
# print(text)

# # Converts to uppercase
# text=text.upper()
# print(text)

# # Converts to Lowecase
# text=text.lower()
# print(text)

# # Replacing a word
# text=text.replace("world", "Python")
# print(text)

# # Spliting a string
# text=text.split()
# print(text)

# Python

# Define the string first
# text = "hello world, I am learning Python!"

# # Check if it starts with "h"
# starts_with_h = text.startswith("h")
# print(starts_with_h)  # True

# # Check if it ends with "Python!"
# ends_with_python = text.endswith("Python!")
# print(ends_with_python)  # True

# # Slicing the string
# print(text[2:5])  # Output: "llo"

# # Printing Hello before text
# print(f"Hello {text}")  

# # List Comparison
# # Compare two lists
# list1= [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# if list1 == list2:
#     print("The lists are equal.")
# else:
#     print("The lists are not equal.")

# print(list1>list2)  # Output: False
# print(list1<list2)  # Output: True

# # Identity Comparison
# print(list1 is list2)  # Output: False
# print(list1 is not list2)  # Output: True

# # Check If One List is a Sublist of Another
# main_list = [1, 2, 3, 4, 5]
# sub_list = [2, 3]

# def is_sublist(small, big):
#     for i in range(len(big) - len(small) + 1):
#         if big[i:i+len(small)] == small:
#             return True
#     return False

# if is_sublist(sub_list, main_list):
#     print("Sublist found in main list.")
# else:
#     print("Sublist not found in main list.")

# Lambda Functions in Python
# A lambda is an anonymous (nameless) one-line function.
# It’s used when you want a quick, small function — usually to pass as an argument.
# lambda arguments: expression

# add= lambda x,y:x+y
# print(add(5,3))  # Output: 8

# square = lambda x: x * x
# print(square(6))  # Output: 36

# # Sort list of tuples by second item
# list_tuples=[(1,2),(3,2),(5,1)]
# list_tuples.sort(key=lambda x: x[1])
# print(list_tuples)  # Output: [(5, 1), (1, 2), (3, 2)]

# # Q.You have a list of numbers. Use a lambda function with map() to create a new list that contains the square of each number.
# numbers = [1, 2, 3, 4, 5]
# square_of_numbers=list(map(lambda x: x**2, numbers))
# print(square_of_numbers)  # Output: [1, 4, 9, 16, 25]

# # Q:Use filter() and a lambda to get only even numbers from the list:
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)  # Output: [2, 4, 6]

# # OOP Basics in Python
# class Dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#     def bark(self):
#         print(f"{self.name} says Woof!")
#     def info(self):
#         print(f"{self.name} is a {self.breed}.")

# dog1 = Dog("Buddy", "Golden Retriever")
# dog1.bark()  # Output: Buddy says Woof!
# dog1.info()  # Output: Buddy is a Golden Retriever.

# # Create a Car class with:

# #     Attributes: brand, year
# #     Method: info() which prints brand and year

# class Car:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#     def info(self):
#         print(f"{self.brand} was manufactured in {self.year}.")
# car1 = Car("Toyota", 2020)
# car1.info()  # Output: Toyota was manufactured in 2020.


# # File Handling in Python
# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a test file.\n")
#     file.close()
# # Reading the file
# with open("example.txt", "r") as file:
#     conetnt = file.read
#     print(conetnt)  # Output: Hello, World!\nThis is a test file.\n

# # Append to the file
# with open("example.txt","a") as file:
#     file.write("Appending a new line.\n")
#     file.close()

# # Try/Except in Python
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print(f"Error: Cannot divide by zero.")

# try:
#     number = int(input("Enter a number: "))
#     print(f"You entered: {number}")
# except ValueError:
#     print("Error: Please enter a valid integer.")
# else:
#     print("No errors occurred.")
# finally:
#     print("Execution completed.")
