"""
============================================
  LECTURE 3 - FILE 4: BOSS CHALLENGE 
  Topics: ALL 6 Topics Combined
  Total Challenges: 
============================================
  These problems combine Lists, Tuples,
  Slicing, and Methods together.
============================================
"""


# ==========================================
#  CHALLENGE 1: The Student Grade Manager 
#  Topics: Lists, List Methods, Slicing, Conditionals
# ==========================================

"""
You are a teacher managing student scores.

Given:
  scores = [45, 78, 92, 55, 88, 33, 95, 67, 71, 60]

Write a program that:
1. Prints the original scores
2. Sorts the scores in descending order (highest first)
3. Prints the TOP 3 scores using slicing
4. Prints the BOTTOM 3 scores using slicing
5. Calculates and prints the average score
   (HINT: sum(scores) / len(scores))
6. Removes all scores below 50 (failing grades)
   HINT: Use .remove() multiple times — count them first!
7. Adds a new score of 100 at the beginning using .insert()
8. Prints the final cleaned and sorted list
9. Uses conditionals to print a message:
   - If average >= 80 → " Excellent class performance!"
   - If average >= 60 → " Good class performance!"
   - If average < 60  → " Class needs improvement!"

"""

scores = [45, 78, 92, 55, 88, 33, 95, 67, 71, 60]

print("================================")
print("    STUDENT GRADE MANAGER")
print("================================")