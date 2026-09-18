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
#     b) Check membership: Is "Python" in ["Java", "C++", "Python"]?
#     c) Check non-membership: Is "Ruby" NOT in the same list?
#     d) What happens if you try [1, 2] * 2.5? Write the error.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 1.  Concatenate two lists
concatenate = list1 + list2
print("concatenation of 2 lists: ", concatenate)

# 2.  Checking membership
lan_list = ["Java" , "C++", "Python"]
print("Is 'Python' available in lan_list: ","Python" in lan_list)

# 3.  Checking non-membership
print("Is 'Ruby' not avaiable in lan_list:", "Ruby" not in lan_list)

# 4.  Repeating a list with a float
"""
[1, 2] * 2.5

can't multiply with other data type value "float" data type must have to be same

"""
#-------------------------------------------------------------------------------------------

# ==========================================
#  PART B: LIST SLICING — POSITIVE
# ==========================================

# Q5. BASIC SLICING [start:stop]:
#     Given: nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     Extract and print:
#     a) First 3 elements
#     b) Elements from index 3 to 7
#     c) Last 4 elements (using positive indices)
#     d) Everything from index 5 to the end
#     e) The entire list using slicing

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. First 3 elements
print("First 3 elements: ", num[0:3])

# 2. Elements formm index 3 to 7
print("3 to 7 elements: ",nums[3:7])

# 3. last 4 elements using positive indices
print("Last  elements: ",nums[6:10])

# 4. Everything from index 5 to the end 
print("5 to end", nums[5:10])

# 5. Entire list using slicing
print("Full: ", nums[ :10])

#-------------------------------------------------------------------------------------------

# Q6. MODIFYING WITH SLICING:
#     Given: data = [10, 'b', 3.14, True, 'e', 50]
#     a) Replace the first 3 elements with ['x', 'y', 'z']
#     b) Delete the last 2 elements using slicing (assign empty list)
#     c) Print the final list

data = [10, 'b', 3.14, True, 'e', 50]

# 1. Replace the first 3 elements
data[0:3] = ['x', 'y', 'z']
print("After Replacement: ",data)

# 2. Delete the last 2 elements
data[4:6] = []
print("After Delete: ",data)

#-------------------------------------------------------------------------------------------

# ==========================================
#  PART C: LIST SLICING — NEGATIVE 
# ==========================================

