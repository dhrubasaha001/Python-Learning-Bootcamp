# # Q: Start with this list. Do the following:
# fruits = ["apple", "banana", "cherry"]

# # - Replace "banana" with "mango"
# # - Add "orange" to the end
# # - Insert "kiwi" at index 1
# # - Remove "cherry"
# # - Print the final list
# fruits[1]='mango'  # Replace "banana" with "mango"
# fruits.append("orange")  # Add "orange" to the end
# fruits.insert(1, "kiwi")  # Insert "kiwi" at index
# fruits.remove("cherry")  # Remove "cherry"
# print(fruits)  # Print the final list

# # Q: Sort this list and print the length:
# numbers = [9, 1, 5, 2, 8]
# # - Sort in ascending
# # - Then descending
# # - Print length of list
# numbers.sort()  # Sort in ascending order
# print("Sorted in ascending:", numbers)
# numbers.sort(reverse=True)  # Sort in descending order
# print("Sorted in descending:", numbers)
# print("Length of list:", len(numbers))  # Print length of list

# # Q: Create a tuple with 5 student names.
# # - Print the 2nd student.
# # - Convert to list and add one more student.
# # - Convert back to tuple and print it.
# my_tuple = ("Alice", "Bob", "Charlie", "David", "Eve")
# print("2nd student:", my_tuple[1])  # Print the 2nd student
# temp_list = list(my_tuple)  # Convert to list
# temp_list.append("Frank")  # Add one more student
# my_tuple = tuple(temp_list)  # Convert back to tuple
# print("Updated tuple:", my_tuple)  # Print the updated tuple

# # Q: Make a set of colors: "red", "blue", "green"
# # - Add "yellow"
# # - Try to add "red" again (what happens?)
# # - Remove "green"
# # - Print the set

# my_color_set = {"red", "blue", "green"}
# my_color_set.add("yellow")  # Add "yellow"
# print("After adding yellow:", my_color_set)
# my_color_set.remove("green")  # Remove "green"
# print("After removing green:", my_color_set)

# # Q: Create a dictionary of student scores:
# scores = {"Alice": 90, "Bob": 85, "Charlie": 92}

# # - Add a new student "David" with score 88
# # - Change "Alice" score to 95
# # - Remove "Bob"
# # - Print final dictionary

# scores['Dhruba']=100
# print("After adding Dhruba:", scores)
# scores['Alice']=95  # Change "Alice" score to 95
# print("After changing Alice's score:", scores)
# scores.pop('Bob')  # Remove "Bob"
# print("After removing Bob:", scores)
# print("Final dictionary:", scores)  # Print final dictionary

# # Q: Given a list of numbers, find the unique ones and store them in a set
# nums = [1, 2, 2, 3, 4, 4, 5]
# # - Print the set of unique numbers
# # - Convert the set back to a list and sort it
# unique_nums = set(nums)  # Find unique numbers and store in a set
# print("Unique numbers set:", unique_nums)
# sorted_unique_nums = sorted(unique_nums)  # Convert set back to sorted list
# print("Sorted unique numbers list:", sorted_unique_nums)
