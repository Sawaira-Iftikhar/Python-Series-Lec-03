"""
============================================
  LECTURE 3 - FILE 2: LIST METHODS
  Topics: append, insert, extend, remove,
          pop, sort, reverse, count, index,
          copy, clear
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: ADDING ELEMENTS 
# ==========================================

# Q1. APPEND vs INSERT vs EXTEND:
#     Given: nums = [1, 2, 3]
#     a) Add 4 to the END  
#     b) Add 99 at INDEX 0 
#     c) Add [7, 8, 9] to the END 
#     d) What happens if you .append([7, 8, 9]) instead of .extend()?
#        Try it on a fresh list and explain the difference.

nums = [1, 2, 3]

# 1. Add 4 to the END 
nums.append(4)
print("After append(4): ",nums)

# 2. Add 99 at index 0 
nums.insert(0, 99)
print("After insert(0, 99): ", nums)

# 3. Add [7, 8, 9] to the END 
nums.extend([7, 8, 9])
print("After extend([7, 8,9]): ",nums)

# 4. Compare append() and extend()
fresh_num = [1,2,3]

fresh_num.append([7, 8,9])
print("After append([7,8,9]): ", fresh_num)

fresh_num = [1, 2, 3]
fresh_num.extend([7, 8, 9])
print("After extend([7, 8, 9]): ", fresh_num)

# append() adds the entire list as ONE element.
# extend() adds each element of the list separately.

#-----------------------------------------------------------------------------------------

# Q2. BUILDING A LIST FROM SCRATCH:
#     Start with an empty list: cart = []
#     Simulate a shopping cart by adding items one by one:
#     a) ("Milk")
#     b) ("Bread")
#     c) (0, "Eggs")  (Eggs are most important!)
#     d) (["Butter", "Cheese"])
#     Print the final cart.

cart = []

# 1. Add Milk
cart.append("Milk")

# 2. Add Bread
cart.append("Bread")

# 3. Add Eggs at index 0
cart.insert(0,"Eggs")

# 4. Add Butter and Cheese
cart.extend(["Butter", "Cheese"])

# Print the final cart 
print("Complete Shopping Cart: ",cart)

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: REMOVING ELEMENTS 
# ==========================================

# Q3. REMOVE vs POP:
#     Given: colors = ["red", "blue", "green", "blue", "yellow"]
#     a) Remove the FIRST "blue" 
#     b) Remove the last element 
#     c) Remove the element at index 1 
#     d) What does .pop() RETURN? Store it in a variable and print.
#     e) What happens if you .remove("purple")? Write the error.

colors = ["red", "blue", "green", "blue", "yellow"]

# 1. Remove the First "blue"
colors.remove("blue")
print("After remove('blue'): ", colors)

# 2. Remove the last Element using pop()
popped_last = colors.pop()
print("Popped Last: ", popped_last ,"---",colors)

# 3. Remove the element at index 1 using pop(1)
pooped_index = colors.pop(1)
print("Popped index 1: ",pooped_index,"---",colors)

# 4. pop() returns the remove element
popped_value = colors.pop()
print(".pop() returns: ",popped_value)

# 5. Q : if you .remove("purple")?

"""
# remove() with a vlaue that does not exist
# colors.remove("purple")
# valueError: list.remove(x): xnot in list

"""

#-----------------------------------------------------------------------------------------

# Q4. CLEAR & DEL:
#     Given: a = [1, 2, 3, 4, 5]
#     a) Delete the element at index 2 using del
#     b) Delete a slice (index 1 to 3) using del
#     c) Clear the entire list using .clear()

a = [1, 2, 3, 4, 5]

# 1. Delete the element at index
del a[2]
print("After del a[1:3]: ",a)

# 2. Delete elements from index 1 to 3
del a[1:3]  # remember index 3 is not included
print("After del a[1:3]: ", a)

# 3. Clear the entire list
a.clear()
print("After clear: ", a)

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART C: SORTING, SEARCHING & MORE 
# ==========================================

# Q5. SORT vs SORTED:
#     Given: nums = [64, 25, 12, 22, 11]
#     a) Sort the list in ASCENDING order 
#     b) Sort in DESCENDING order
#     c) Create a NEW sorted list 
#        changing the original
#     d) What does .sort() return? Try: result = nums.sort()
#        Print result. Explain WHY it's None.

nums = [64, 25, 12, 22, 11]

# 1. Sort the list in ascending order
nums.sort()
print("Ascending: ",nums)

# 2. Sort the list in Decending order
nums.sort(reverse=True)
print("Decending: ",nums)

# 3. Created a New sorted list 
# make a fres original list for this part.
original = [65, 78, 11, 24, 22]

sorted_nums = sorted(original)

print("sorted() new list ", sorted_nums)
print("Original unchanged: ",original)

# 4. What does .sort() return?
result = nums.sort()
print(".sort() returns: ",result)

"""
# .sort() changes the original list directly
# It does not create and return a new list
# Therefore, .sort() returns None.

"""

#-----------------------------------------------------------------------------------------

# Q6. COUNT & INDEX:
#     Given: fruits = ["apple", "banana", "apple", "cherry", "apple", "date"]
#     a) Count how many times "apple" appears
#     b) Find the index of FIRST "apple"
#     c) Find the index of "cherry" 
#     d) What happens if you search for "mango"? 

fruits = ["apple", "banana", "apple", "cherry", "apple", "date"]

# 1. Count how many times "apple" appears
apple_count = fruits.count("apple")
print('Count of "apple": ', apple_count)

# 2. find the index of the first "apple"
first_apple = fruits.index("apple")
print('First "apple" at: ',first_apple, "index")

# 3. Find the index of "cherry"
cherry_index = fruits.index("cherry")
print('The "cherry" is at: ',cherry_index, "index")

# 4. Search of "mango"
mango_index = fruits.index("mango")
print("the mango index is: ",mango_index)  # it will show error 

#-----------------------------------------------------------------------------------------

# Q7. COPY — Shallow vs Direct Assignment:
#      Given: original = [1, 2, [3, 4], 5]
#      a) Create a direct copy: 
#      b) Create a shallow copy:
#      c) Change original[0] to 99
#      d) Change original[2][0] to 888 (nested change)

original = [1, 2, [3, 4], 5]

# 1. Direct Assignment
copy1 = original

# 2. Shallow copy
copy2 = original.copy()

# 3. Change an element in the outer list
original[0] = 99


