# # Variable and Data Type
# integer = 10
# float_number = 10.5
# string = "Hello, World!"
# boolean = True
# print(type(integer),type(float_number),type(string),type(boolean), sep=" \n ")  

# # Input and Output
# name = input("Enter your name: ")
# print("Hello,", name)

# # Operators
# num_1=int(input("Enter first number: "))
# num_2=int(input("Enter second number: "))
# print("Addition:", num_1 + num_2)
# print("Subtraction:", num_1 - num_2)
# print("Multiplication:", num_1 * num_2)
# print("Division:", num_1 / num_2)
# print("Modulus:", num_1 % num_2)
# print("Exponentiation:", num_1 ** num_2)
# print("Floor Division:", num_1 // num_2)
# print("Comparison:", num_1 == num_2)
# print("Greater than:", num_1 > num_2)
# print("Less than:", num_1 < num_2)
# print("Logical AND:", num_1 > 5 and num_2 < 10)
# print("Logical OR:", num_1 > 5 or num_2 < 10)
# print("Logical NOT:", not (num_1 > 5))

# # Control Structures
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# Loops
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()  # New line after each row

# for i in range (5):
#     for j in range(5 - i):
#         print("*", end="")
#     print()  # New line after each row

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()  # New line after each row

# While Loop
# count =0
# while count < 5:
#     print("Count is:", count)
#     count += 1  # Increment count by 1

# Functions
# def greet(name):
#     """Function to greet a person."""
#     return f"Hello, {name}!"

# name= input("Enter your name: ")
# print(greet(name))

# def add_number(num1,num2):
#     """Function to add two numbers."""
#     return num1 + num2

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum:", add_number(num1, num2))

# # List and Its Methods
# my_list = [1, 2, 3, 4, 5]
# print("Original List:", my_list)
# print("Length of List:", len(my_list))  # Length of the list
# print("First Element:", my_list[0])  # Accessing the first element
# print("Last Element:", my_list[-1])  # Accessing the last element
# print("Sliced List (0 to 2):", my_list[0:3])
# print("Sliced List (2 to end):", my_list[2:])  # Slicing from index 2 to the end
# print("Sliced List (start to 3):", my_list[:3])  # Slicing from start to index 3
# print("Reversed List:", my_list[::-1])
# my_list.append(6)  # Add an element to the end
# print("After Append:", my_list)
# my_list.insert(0, 0)  # Insert an element at index 0
# print("After Insert:", my_list)
# my_list.remove(3)  # Remove the first occurrence of 3
# print("After Remove:", my_list)
# my_list.pop()  # Remove the last element
# print("After Pop:", my_list)
# my_list.sort()  # Sort the list
# print("After Sort:", my_list)
# my_list.reverse()  # Reverse the list
# print("After Reverse:", my_list)
# my_list.clear()  # Clear the list
# print("After Clear:", my_list)
# my_list_1=['Dppledscs', 'Vanana', 'cherry']
# my_list_1.sort(key=len)  # Sort the list
# print("Sorted List:", my_list_1)

# Tuple and Its Methods
# my_tuple = (1, 2, 3, 4, 5)
# print("Original Tuple:", my_tuple)
# print("Length of Tuple:", len(my_tuple))  # Length of the tuple
# print("First Element:", my_tuple[0])  # Accessing the first element
# print("Last Element:", my_tuple[-1])  # Accessing the last element
# print("Sliced Tuple (0 to 2):", my_tuple[0:3])
# print("Sliced Tuple (2 to end):", my_tuple[2:])  # Slicing from index 2 to the end
# print("Sliced Tuple (start to 3):", my_tuple[:3])  # Slicing from start to index 3
# print("Reversed Tuple:", my_tuple[::-1])
# # Tuples are immutable, so we cannot modify them
# # However, we can convert to a list, modify, and convert back to a tuple
# temp_list = list(my_tuple)
# temp_list.append(6)  # Add an element to the end
# my_tuple = tuple(temp_list)
# print("After Append:", my_tuple)
# temp_list.insert(0, 0)  # Insert an element at index 0
# my_tuple = tuple(temp_list)
# print("After Insert:", my_tuple)
# temp_list.remove(3)  # Remove the first occurrence of 3
# my_tuple = tuple(temp_list)
# print("After Remove:", my_tuple)
# temp_list.pop()  # Remove the last element      
# my_tuple = tuple(temp_list)
# print("After Pop:", my_tuple)
# temp_list.sort()  # Sort the list
# my_tuple = tuple(temp_list)
# print("After Sort:", my_tuple)
# temp_list.reverse()  # Reverse the list
# my_tuple = tuple(temp_list)
# print("After Reverse:", my_tuple)
# temp_list.clear()  # Clear the list
# my_tuple = tuple(temp_list)
# print("After Clear:", my_tuple)

# Set and Its Methods
# my_set = {1, 2, 3, 4, 5}
# print("Original Set:", my_set)
# print("Length of Set:", len(my_set))  # Length of the set
# print("Is 3 in Set?", 3 in my_set)  # Check if an element is in the set
# print("Is 6 in Set?", 6 in my_set)
# my_set.add(6)  # Add an element to the set
# print("After Add:", my_set)
# my_set.remove(3)  # Remove an element from the set
# print("After Remove:", my_set)
# my_set.discard(4)  # Discard an element (no error if not found)
# print("After Discard:", my_set)
# my_set.pop()  # Remove an arbitrary element from the set
# print("After Pop:", my_set)
# my_set.clear()  # Clear the set
# print("After Clear:", my_set)

# # Dictionary and Its Methods
# my_dictonary = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print("Original Dictionary:", my_dictonary)
# print("Keys:", my_dictonary.keys())  # Get all keys
# print("Values:", my_dictonary.values())  # Get all values
# print("Items:", my_dictonary.items())  # Get all key-value pairs
# print("Name:", my_dictonary['name'])  # Access value by key
# my_dictonary['age'] = 31  # Update value for a key
# print("Updated Age:", my_dictonary['age'])
# my_dictonary['country'] = 'USA'  # Add a new key-value pair
# print("After Adding Country:", my_dictonary)
# my_dictonary.pop('city')  # Remove a key-value pair
# print("After Removing City:", my_dictonary)
# my_dictonary.clear()  # Clear the dictionary
# print("After Clear:", my_dictonary)