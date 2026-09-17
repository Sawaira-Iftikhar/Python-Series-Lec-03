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