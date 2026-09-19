# Python-Series-Lec-03
A collection of Python programs and practice exercises covering the fundamentals of lists and tuples, including indexing, positive and negative slicing, and commonly used list and tuple methods.

## 📚 Topics Covered

| # | Topic | Status |
|---|-------|:------:|
| 1 | List Basics (Creation, Access, Mutability) | ✅ |
| 2 | List Slicing (Positive & Negative) | ✅ |
| 3 | List Methods | ✅ |
| 4 | Tuple Basics (Creation, Access, Immutability) | ✅ |
| 5 | Tuple Slicing (Positive & Negative) | ✅ |
| 6 | Tuple Methods | ✅ |



## 📂 Practice Files

| File | Topics |  Questions |
|------|--------|:---------:|
| [01_Lists_Basics.py](01_Lists_Basics.py) | List Basics, List Slicing (Positive & Negative) |  08 |
| [02_List_methods.py](02_List_methods.py) | List Methods (add, remove, sort, etc.) |  07 |
| [03_Tuples.py](03_Tuples.py) | Tuple Basics, Tuple Slicing, Tuple Methods |  04 |
| [04_Challenge.py](04_Challenge.py) | ALL Topics Mixed (Boss Level) | 0  |



## 💡 Quick Cheat Sheet (Lecture 3 Highlights)

<details>
<summary><b>Click to expand quick revision notes</b></summary>

<br>

### 1. List vs Tuple — Key Differences

| Feature | List `[]` | Tuple `()` |
|---------|-----------|------------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Methods | Many (append, pop, sort…) | Only 2 (count, index) |
| Speed | Slower | Faster |
| Use Case | Data that changes | Data that stays fixed |
| Memory | More | Less |

### 2. List Slicing


 | 10 | 20 | 30 | 40 | 50 | 
|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 |← Positive Index 
|-5 |-4 |-3 |-2 |-1 |← Negative Index

**Positive Index →** left to right: `0 1 2 3 4`  
**Negative Index →** right to left: `-1 -2 -3 -4 -5`

```text

nums = [10, 20, 30, 40, 50]

nums[1:4]    # [20, 30, 40]
nums[:3]     # [10, 20, 30]
nums[2:]     # [30, 40, 50]
nums[::-1]   # [50, 40, 30, 20, 10]  (reverse)
nums[-3:]    # [30, 40, 50]
nums[::2]    # [10, 30, 50]  (every 2nd)
``` 

### 3. Most Used List Methods
| Method |	Description	| Example |
|--------|----------|---------|
|`.append(x)`|	Adds item to end |	`lst.append(5)`|
|`.insert(i, x)`|	Inserts at index|	`lst.insert(0, 99)`|
|`.extend(iter)`|	Adds multiple items	|`lst.extend([7, 8])`|
|`.remove(x)`|	Removes first match	|`lst.remove(20)`|
|`.pop(i)`|	Removes & returns item|	`lst.pop(-1)`|
|`.sort()`|	Sorts in place|	`lst.sort(reverse=True)`|
|`.reverse()`|	Reverses in place|`lst.reverse()`|
|`.count(x)`|	Counts occurrences|	`lst.count(3)`|
|`.index(x)`|	Index of first match|	`lst.index(20)`|
|`.copy()`|	Shallow copy	|`new = lst.copy()`|
|`.clear()`|	Empties the list|	`lst.clear()`|

```
# ❌ Tuples are immutable — this will ERROR
t = (1, 2, 3)
t[0] = 99        # TypeError!

# ❌ Single element tuple needs a comma
t = (5)          # This is an int, NOT a tuple!
t = (5,)         # ✅ This is a tuple

# ❌ .sort() returns None — it sorts in place
nums = [3, 1, 2]
result = nums.sort()
print(result)    # None! Use sorted(nums) instead
``` 