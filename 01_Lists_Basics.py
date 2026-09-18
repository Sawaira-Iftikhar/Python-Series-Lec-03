"""
============================================
  LECTURE 3 - FILE 1: LISTS BASICS & SLICING
  Topics: List Creation, Access, Slicing (+/-)
  Total Questions: 
============================================

"""

# ==========================================
#  PART A: LIST BASICS 
# ==========================================

# Q1. Create the following lists and print each with its type:
#     a) A list of 5 integers
#     b) A list of 3 strings (your favorite languages)
#     c) A mixed list (int, float, str, bool)
#     d) An empty list
#     e) A nested list (list inside a list)

# 1.  List of 5 integer
num = [10 , 20, 30, 40, 50]
print(num, type(num))

# 2.  List of 3 string
languages = ["Python", "C++", "Java"]
print(languages, type(languages))

# 3. list of mixed data type list
mixed_list = [25, 3.14, "Python", True]
print(mixed_list, type(mixed_list))

# 4.  Empty list
empty_list = []
print(empty_list, type(empty_list))

# 5.  Nested list
nested_list = [[1, 2, 3], ["Python", "C++"]]
print(nested_list, type(nested_list))

#----------------------------------------------------------------------------------------------------

# Q2. ACCESSING ELEMENTS:
#     Given: fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#     a) Print the first fruit
#     b) Print the last fruit using positive index
#     c) Print the last fruit using negative index
#     d) Print the middle fruit
#     e) What is the length of this list?

fruits = ["apple", "banana", "cherry", "date", "strawberry"]

# a) First fruit
print("First:", fruits[0])

# b) last fruit with positive index
print("Last (positive): ", fruits[4])

# c) Last fruit with negative index
print("Last (negative): ", fruits[-1])

# d) Middle fruit
print("MIddle: ", fruits[2])

# e) Length of the list
print("Length: ",len(fruits))

#--------------------------------------------------------------------------------------------------

# Q3. MUTABILITY — Lists can be changed:
#     Given: colors = ["red", "green", "blue"]
#     a) Change "green" to "yellow" using index
#     b) Change the last color to "purple"
#     c) Print the modified list

colors = ["red", "green", "blue"]
print("Original list of colors: ",colors)

# Change "green" to "yellow"
colors[1] = "yellow"
print("After changing the 1 index: ",colors)

#Change the last color to purple
colors[len(colors) - 1] = "purple"

#  colors[len(colors)] = "purple"   this method is wrong 

#Other two methods
""" 
colors[-1] = 'purlpe'
colors[2] = 'purple'

"""
print("After the last color change: ",colors)

#-------------------------------------------------------------------------------------------

# Q4. LIST OPERATIONS:
#     a) Concatenate two lists: [1, 2, 3] + [4, 5, 6]
#     b) Repeat a list: ["Ha"] * 4
#     c) Check membership: Is "Python" in ["Java", "C++", "Python"]?
#     d) Check non-membership: Is "Ruby" NOT in the same list?
#     e) What happens if you try [1, 2] * 2.5? Write the error.
