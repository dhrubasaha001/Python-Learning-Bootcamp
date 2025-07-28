# # List comprehension
# my_list=[]
# for i in range(1,10):
#     my_list.append(i**2)
# print("List using for loop:", my_list)

# my_list = [i**2 for i in range(1, 10)]
# print("List using list comprehension:", my_list)

# # Even numbers from 0–19
# even= [i for i in range(20) if i%2==0]
# print("Even numbers from 0 to 19:", even)

# # Conditional list: even → "Even", odd → "Odd"
# conditional_list=["Even" if i%2==0 else "Odd" for i in range(20)]
# print("Conditional list:", conditional_list)

# # Dictionary Comprehension
# my_dictionary= {i: i**2 for i in range(1, 6)}
# print("Dictionary using comprehension:", my_dictionary)

# orginal_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dictionary = {k: v**2 for k, v in orginal_dict.items()}
# print("New dictionary with squared values:", new_dictionary)

# # Advance OOP Concepts in Python
# # Inheritance
# # Inheritance allows a class to inherit attributes and methods from another class.
# # It promotes code reusability and establishes a relationship between classes.
# # Inheritance Example
# class Person:
#     def __init__(self,name):
#         self.name=name;
#     def speak(self):
#         return f"Hello, my name is {self.name}."
# class Student(Person):
#     def study(self):
#         return f"{self.name} is studying."

# s1 = Student("Alice")
# print(s1.speak())  # Output: Hello, my name is Alice.
# print(s1.study())  # Output: Alice is studying.

# # polymorphism
# # # Polymorphism allows methods to do different things based on the object it is acting upon
# # # It allows for methods to be defined in a base class and overridden in derived classes.
# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class Dog(Animal):
#     def speak(self):
#         return "Dog barks"
# class Cat(Animal):
#     def speak(self):
#         return "Cat meows"

# for pet in [Dog(), Cat()]:
#     pet.speak() # Output: Dog barks, Cat meows
#     print(pet.speak())

# print(Dog().speak())  # Output: Dog barks
# print(Cat().speak())  # Output: Cat meows

# Encapsulation
# Encapsulation is the bundling of data and methods that operate on that data within a single
# unit, or class. It restricts direct access to some of an object's components.
# This is a means of preventing unintended interference and misuse of the methods and data.
# class BankAccount:
#     def __init__ (self):
#         self._balance = 1000  # Protected attribute
#         self.__pin = 1234  # Private attribute
#     def show_pin(self):
#         return self.__pin

# acc= BankAccount()
# print("Balance:", acc._balance)  # Accessing protected attribute
# print("Pin:", acc.show_pin())  # Accessing private attribute through a method

# class BankAccount:
#     def __init__(self, account_holder, initial_balance):
#         self.account_holder = account_holder  # Public attribute
#         self.__balance = initial_balance     # Private attribute (by convention)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient balance.")

#     def get_balance(self):
#         return self.__balance

# # Usage
# my_account = BankAccount("Alice Smith", 1000)

# print(f"Account Holder: {my_account.account_holder}")

# # Attempting to directly access the private attribute (will not work as expected)
# # print(my_account.__balance) # This will raise an AttributeError

# # Accessing and modifying the balance through public methods
# my_account.deposit(200)
# my_account.withdraw(500)

# # Getting the balance using the public getter method
# print(f"Current balance: {my_account.get_balance()}")


# #  @staticmethod vs @classmethod
# # A static method does not require an instance of the class to be called.
# # It is defined using the @staticmethod decorator.
# # A class method is bound to the class and not the instance of the class.
# # It is defined using the @classmethod decorator and takes the class as the first argument.
# class MathOperations:
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @classmethod
#     def info(cls):
#         return f"This class performs basic math operations. Class name: {cls.__name__}"
    
# print(MathOperations.add(5, 3))  # Output: 8
# print(MathOperations.info())  # Output: This class performs basic math operations. Class name: MathOperations


# 