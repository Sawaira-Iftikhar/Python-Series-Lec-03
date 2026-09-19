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


colors = ("red", "green", "blue", "yellow", "purple")

# 1. Print the first color
print("First color: ",colors[0])

# 2. Print the last color using negative index
print("Last color: ",colors[-1])

# 3. Print the length of the tuple
print("length of tuple: ",len(colors))

# 4. Check if "blue" is in the tuple
print('"blue" in tuple: ',"blue" in colors)

## 5. Check if "orange" is not in the tuple
print('"orange" not in tuple: ', "orange" not in colors)

#----------------------------------------------------------------------------------------

# ==========================================
#  PART B: TUPLE SLICING 
# ==========================================

"""
Tuple slicing and list slicing both are excatly are same not a little bit is change 

One major difference:

as you can change the value of index in list 
But in tuple we can not chagne the value of index just like string 

OK! I Hope you get it.
"""

# ==========================================
#  PART C: TUPLE METHODS 
# ==========================================

# Q3. COUNT & INDEX (The ONLY 2 tuple methods):
#     Given: nums = (1, 2, 3, 2, 4, 2, 5, 2)
#     a) Count how many times 2 appears 
#     b) Count how many times 9 appears 
#     c) Find the index of first 2 
#     d) What happens if you .index(99)? Write the error.

nums = (1, 2, 3, 2, 4, 2, 5, 2)

# 1. Count how many times 2 appears
count_2 = nums.count(2)
print("Count of 2: ", count_2)

# 2. Count how many times 9 appear
count_9 = nums.count(9)
print("Count of 9: ", count_9)

# 4.  Find the index of first 2 
index_2 = nums.index(2)
print("index of 2: ", index_2)

# 5. Search for 99
# nums.index(99)
# ValueError: tuple.index(x): x not in tuple