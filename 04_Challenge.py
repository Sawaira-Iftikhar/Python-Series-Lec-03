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

# 1. Print the original scores
print("Original: ",scores)

# 2. Sort scores in descening order
scores.sort(reverse=True)
print("Sorted(desc): ",scores)

# 3. Print TOP 3 scores
top = scores[:3]
print("Top 3: ", top)

# 4. Print Bottom 3 scores
bottom = scores[-3:]
print("Bottom 3:", bottom)

# 5. Calculate the average
average = sum(scores) / len(scores)
print("Average:", average)

# 6. Remove all scores below 50
# Count the failing scores first
failing_count = 0

for score in scores:
    if score < 50:
        failing_count += 1

# Remove each failing score
for score in scores.copy():
    if score < 50:
        scores.remove(score)

print("Failing grades removed:", failing_count)

# 7. Add 100 at the beginning
scores.insert(0, 100)

# 8. Print the final cleaned and sorted list
print("After adding 100:", scores)

# 9. Check class performance
if average >= 80:
    print("Excellent class performance!")
elif average >= 60:
    print("Good class performance!")
else:
    print("Class needs improvement!")

print("================================")

#-------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 2: The Playlist Manager 
#  Topics: Lists, Tuples, Methods, Slicing, Conversion
# ==========================================

"""
You are building a music playlist system.

Given:
  playlist = ["Bohemian Rhapsody", "Stairway to Heaven",
              "Hotel California", "Imagine", "Yesterday"]
  favorites = ("Bohemian Rhapsody", "Imagine")  # Tuple — can't change!

Write a program that:
1. Prints the current playlist with numbering
   (Use indexing to print: "1. Bohemian Rhapsody", etc.)
2. Adds "Let It Be" to the END of the playlist
3. Inserts "Hey Jude" at position 2
4. Removes "Yesterday" from the playlist
5. Checks which songs in the playlist are also in favorites
   (Use 'in' operator — check each song manually since no loops yet)
   Print: " 'Bohemian Rhapsody' is a favorite!"
6. Creates a REVERSED copy of the playlist using slicing
7. Converts the favorites tuple to a list, adds "Hey Jude" to it,
   then converts it back to a tuple
8. Prints the final playlist and updated favorites

"""

playlist = [
    "Bohemian Rhapsody",
    "Stairway to Heaven",
    "Hotel California",
    "Imagine",
    "Yesterday"
]

favorites = ("Bohemian Rhapsody", "Imagine")

print("================================")
print("     PLAYLIST MANAGER")
print("================================")

# 1. Print the current playlist with numbering
print("Current Playlist:")

print("  1.", playlist[0])
print("  2.", playlist[1])
print("  3.", playlist[2])
print("  4.", playlist[3])
print("  5.", playlist[4])

print("--------------------------------")

# 2. Add "Let It Be" to the end
playlist.append("Let It Be")
print('After adding "Let It Be":', playlist)

# 3. Insert "Hey Jude" at position 2
# Position 2 means index 1.
playlist.insert(1, "Hey Jude")
print('After inserting "Hey Jude":', playlist)

# 4. Remove "Yesterday"
playlist.remove("Yesterday")
print('After removing "Yesterday":', playlist)


print("--------------------------------")
