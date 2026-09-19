"""
============================================
  LECTURE 3 - FILE 3: TUPLES
  Topics: Tuple Basics, Tuple Slicing, Tuple Methods
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: TUPLE BASICS 
# ==========================================

# Q1. CREATING TUPLES:
#     Create and print the following tuples with their type:
#     a) A tuple of 5 integers
#     b) A tuple of 3 strings
#     c) A mixed tuple (int, float, str, bool)
#     d) An empty tuple
#     e) A SINGLE element tuple (TRICKY! use a comma)
#     f) A tuple WITHOUT parentheses (tuple packing)


# 1. Tuple of 5 integers
num = (1, 2, 3, 4, 5)
print("Tuple of 5 integer: ",num,type(num))

# 2. Tuple of 3 strings
letters = ("a", "b", "c")
print("Tuple of 3 string: ",letters,type(letters))

# 3. Empty Tuple
empty = ()
print("Empty tuple; ",empty,type(empty))

# 4. Mixed tuple
mixed = (10, 3.4, "hello", True)
print("Mixed datatype Tuple: ",mixed,type(mixed))

# 5. Single-element tuple
single = (5,)
print("Single element: ",single,type(single))

# 6. tuple withoit parenthese (tuple packing)
packed = 1, 2, 3
print("Tuple without Parenthese: ",packed,type(packed))

#-----------------------------------------------------------------------------------------

# Q2. ACCESSING ELEMENTS:
#     Given: colors = ("red", "green", "blue", "yellow", "purple")
#     a) Print the first color
#     b) Print the last color using negative index
#     c) Print the length of the tuple
#     d) Check if "blue" is in the tuple using 'in'
#     e) Check if "orange" is NOT in the tuple
