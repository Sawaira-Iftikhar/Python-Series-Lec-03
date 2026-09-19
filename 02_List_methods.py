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
#     a) Remove the FIRST "blue" using 
#     b) Remove the last element using 
#     c) Remove the element at index 1 using 
#     d) What does .pop() RETURN? Store it in a variable and print.
#     e) What happens if you .remove("purple")? Write the error.

colors = ["red", "blue", "green", "blue", "yellow"]

# 1. Remove the First