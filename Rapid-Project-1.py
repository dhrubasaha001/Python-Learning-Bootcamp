# # Simple Calculator
# # This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero"
#     return x / y
# # Main function to run the calculator
# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#     choice = input("Enter choice (1/2/3/4/5): ")
    
#     if choice in ['1', '2', '3', '4', '5']:
#         if choice == '5':
#             print("Exiting the calculator.")
#             return
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         while True:
#             if choice == '1':
#                 print(f"{num1} + {num2} = {add(num1, num2)}")
#                 break
#             elif choice == '2':
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
#                 break
#             elif choice == '3':
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
#                 break
#             elif choice == '4':
#                 result = divide(num1, num2)
#                 if result == "Cannot divide by zero":
#                     print(result)
#                     break
#                 else:
#                     print(f"{num1} / {num2} = {result}")
#                     break  
#             elif choice == '5':
#                 print("Exiting the calculator.")
#                 break
#             else:
#                 print("Invalid input")
#                 break
#     else:
#         print("Invalid choice. Please select a valid operation.")

# # Run the calculator
# if __name__ == "__main__":
#     calculator()
    


# my_passwords = {'Facebook': 'fb123', 'Twitter': 'twit456', 'Instagram': 'inst789'}

# platform = input("Enter the platform you want to login to: ")
# password = input("Enter your password: ")

# if platform in my_passwords:
#     if my_passwords[platform] == password:
#         print("Password Matched")
#         print(f"Logged in to {platform}")
#     else:
#         print("Incorrect Password")
# else:
#     print("Platform not found")

