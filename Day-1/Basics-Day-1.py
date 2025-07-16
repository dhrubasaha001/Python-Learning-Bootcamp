# #Python Variables
# # Variables are like little containers to store data.
# # ✅ name is a string (text).
# # ✅ age is an integer (whole number).
# # ✅ temperature is a float (decimal).
# # ✅ is_sick is a boolean (True or False).
#
# name="Dhruba Saha"
# age=19
# temperature=101
# is_sick=True
#
# # Type of all the Variables using Type function
# print(type(name))
# print(type(age))
# print(type(temperature))
# print(type(is_sick))
#
# # Printing Varibles
# print("Name:", name)
# print("Age:", age)
# print("Temperature:", temperature)
# print("Is Sick:", is_sick)

# Operators in Python
# operators are special symbols that tell the compiler or interpreter to perform specific mathematical, logical, or other operations.
# ✅ Arithmetic Operators
# E.g., +, -, *, /, //, %, **
# Arithmetic operators are used to do simple maths operations such as multiplication , subtraction , addition , division , integer division , remainder and  power .
#
number_1 = 3
number_2 = 2
#
# print("Addition:",number_1+number_2)
# print("Subtraction:",number_1-number_2)
# print("Multiplication:",number_1*number_2)
# print("Division: ", number_1/number_2)
# print("Integer Division :",number_1 // number_2)
# print("Remainder: ",number_1 % number_2)
# print("Power: ",number_1**number_2)


# # ✅ Comparison Operators
# # E.g., ==, !=, <, >, <=, >=
# # Comparison Operator is used to compare variables in Python '==' means equal to '!=' means not equal to '<=' means less than equal to '>=' means greater than equal to '<' and '>' means less than or greater than .
# print("'==' Equal to :",number_1==number_2)
# print("'!=' Not Equal to :",number_1!=number_2)
# print("'<=' less than equal to:",number_1<=number_2)
# print("'<' less than:",number_1<=number_2)
# print("'>=' greater than equal to:",number_1>=number_2)
# print("'>' greater than :",number_1>number_2)


# ✅ Logical Operators
# E.g., and, or, not
# Used to combine conditional statements. These are and, or, and not.
# AND do like that if both condition true it returns true if one condition is false it will return false
# OR do like that if both condition is false it return false if one condition is true it will return true
# NOT do like that if a condition is false it will change it to true and if the condition is true it will change it in false.

# x = True
# y = False
# print("AND:", x and y)
# print("OR:", x or y)
# print("NOT X:", not x)

#  ✅ Identity Operators
# Check if two variables point to the same object in memory:
# Operator	Description
# is	Same object?
# is not	Not the same object?
#
# x=[1,2,3]
# y=x
# z=[1,2,3]
#
# print("X is Y:",x is y)
# print("Y is X:",y is x)
# print("X is not Y:",x is not y)
# print("Y is X:",y is not x)
# print("X is Z :", x is z)
# print("Z is X :", z is x)
# print("X is not Z:",x is not z)
# print("Z is not X:",z is not x)
# # Because the both are same as we see but we did not did it z=x
# z=x
# print("X is Z :", x is z)
# print("Z is X :", z is x)
# print("X is not Z:",x is not z)
# print("Z is not X:",z is not x)
#
# # 🌿 ✅ Membership Operators
# # Check if a value exists in a sequence:
# # | Operator | Description    |
# # | -------- | -------------- |
# # | `in`     | Value present? |
# # | `not in` | Value absent?  |
# list[str]=["apple","banana","grapes"]
# print("apple" in list)       # True
# print("mango" not in list)   # False

# # 🌿 ✅ Bitwise Operator
# # Bitwise operators in Python are used to perform operations directly on the binary representations of integers. They manipulate individual bits (0s and 1s) within a number.
# # | Operator | Description | Example (`a=5`, `b=3`) |     |         |
# # | -------- | ----------- | ---------------------- | --- | ------- |
# # | `&`      | Bitwise AND | `a & b` → `1`          |     |         |
# # | \`       | \`          | Bitwise OR             | \`a | b`→`7\` |
# # | `^`      | Bitwise XOR | `a ^ b` → `6`          |     |         |
# # | `~`      | Bitwise NOT | `~a` → `-6`            |     |         |
# # | `<<`     | Left Shift  | `a << 1` → `10`        |     |         |
# # | `>>`     | Right Shift | `a >> 1` → `2`         |     |         |
#
# a = 5  # binary: 0101
# b = 3  # binary: 0011
#
# print("a & b:", a & b)
# print("a | b:", a | b)
# print("a ^ b:", a ^ b)
# print("~a:", ~a)
# print("a << 1:", a << 1)
# print("a >> 1:", a >> 1)




# # Conditional Statement
# # if , elif , else
# if temperature > 100 :
#     print("You have fever rest on Lucy's Lap.")
# elif temperature == 100:
#     print("You need to take care of your health you are on border line of fever.")
# else:
#     print("You are all right.")
#
# # Loops 'for' loop for ( initialization , range , jump )
# i=1
# for i in range(10):
#     print("Hello World!")
# #   'While' loop is a control loop where need to give Increament and decreament , initialization of the interable:
# while i<=10:
#     print("Hello World!")
#     i=i+1
