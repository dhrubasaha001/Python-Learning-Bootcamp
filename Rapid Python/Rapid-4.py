# JSON Handling (with json module)
# What is JSON?
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for
# humans to read and write, and easy for machines to parse and generate. It is often
# used to transmit data between a server and a web application as an alternative to XML.
# It is language-independent and can be used with many programming languages, including Python.
# class. It restricts direct access to some of the object's components.
# import json
# data={
#     "name":"Dhruba Saha",
#     "age": 19,
#     "city": "Kolkata",
#     "hobbies": ["reading", "coding", "gaming"]
# }
# json_string = json.dumps(data)
# print(json_string) # Convert Python object to JSON string

# # Convert JSON to Python (loads)
# json_data='{"name": "Dhruba Saha", "age": 19, "city": "Kolkata", "hobbies": ["reading", "coding", "gaming"]}'
# data = json.loads(json_data)
# # print(data)  # Convert JSON string to Python object
# # print(data['name'])  # Accessing data from the Python object
# with open('data.json', 'w') as f:
#     json.dump(data, f)  # Write Python object to a JSON file
# with open('data.json', 'r') as f:
#     data_from_file = json.load(f)  # Read JSON data from a file



# Regex (Regular Expressions)
# What is Regex?
# Regular expressions (regex or regexp) are sequences of characters that form a search pattern.
# They are used for string searching and manipulation, allowing for complex pattern matching.
# import re 
# # text="9474515462"
# # numbers=re.findall(r"\d{10}",text)
# # print("10-digit numbers found:", numbers)

# email="dhruba@gmail.com"
# pattern=r"\w+@\w+\.\w+"
# if re.match(pattern, email):
#     print("Valid email address")
# else:
#     print("Invalid email address")
# if re.search(pattern, email):
#     print("Email address found in the text")
# else:
#     print("Email address not found in the text")

# Task

# You have a non-empty set S
# , and you have to execute N commands given in
# N lines.
# The commands will be pop, remove and discard.

# n=int(input("Enter the number of commands: "))
# s = set(map(int, input("Enter the elements of the set: ").split()))
# for _ in range(n):
#     command = input("Enter command: ").strip().split()
#     cmd = command[0]
    
#     if cmd == "pop":
#         if s:
#             s.pop()
#     elif cmd == "remove":
#         if len(command) > 1:
#             element = int(command[1])
#             s.remove(element)
#     elif cmd == "discard":
#         if len(command) > 1:
#             element = int(command[1])
#             s.discard(element)
# print("Final set:", s)