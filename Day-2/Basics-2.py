# # Day 2 List , Tuples, Sets, Dictionaries
# # List 
# # List is a collection of items in a particular order.
# # Lists are mutable, meaning you can change their content without changing their identity.
# # Creating a list 

# fruits=['apple','banana','grapes']
# # Printing a List
# print(fruits)
# # Adding fruits at a specific index or position //We are just replacing 
# fruits[1]='mango'
# print(fruits)
# # Adding fruit at last position
# fruits.append('guava')
# print(fruits)
# # Adding specific item on a specific index 
# fruits.insert(1,'pineapple')
# print(fruits)
# # removing item on a specific iteam
# fruits.remove('guava')
# print(fruits)
# # Removing item on a specific index
# fruits.pop(1)
# print(fruits)

# list1=[1,2,5,4,6]
# Sorting a list in ascending order
# list1.sort(key=None,reverse=False)
# print(list1)
# Sorting a list in descending order
# list1.sort(reverse=True)
# print(list1)

# Sorting a list on char length
# words=['banana','apple','kiwi']
# words.sort(key=len)
# print(words)

# # Check if item exists
# print('apple' in fruits)  # True or False

# # Length of list
# print(len(fruits))  # Number of elements

# # Check if item exists
# print('apple' in fruits)  # True or False

# # Length of list
# print(len(fruits))  # Number of elements

# # Looping with index and item
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

