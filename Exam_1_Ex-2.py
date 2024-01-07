def sumParts(n):
    n_str = str(n)
    length = len(n_str)
    
    if length % 2 == 0:
        middle = length // 2
        left_half = n_str[:middle]
        right_half = n_str[middle:]
    else:
        middle = (length + 1) // 2
        left_half = n_str[:middle - 1]
        right_half = n_str[middle - 1:]
    
    # Convert empty strings to 0 before converting to int
    left_half = int(left_half) if left_half else 0
    right_half = int(right_half) if right_half else 0
    
    return left_half + right_half

# Test cases
print(sumParts(1234))  # Output: 46
print(sumParts(8))     # Output: 8
print(sumParts(123))   # Output: 24

# ---------------------------//--------------------------------------------

from random import randint
from sudokuUtils import containsConsecutive

# Create a list with 3 lists with 3 integers each filled with random numbers from 1 to 9
random_list:list = [[randint(1, 9) for _ in range(3)] for _ in range(3)]

# Print the list to the console
print("Generated List:")
for sublist in random_list:
    print(sublist)

# Check if it's a Sudoku block and print the result
if containsConsecutive(random_list):
    print("YES, it is a Sudoku block")
else:
    print("NOT a Sudoku block")

# ---------------------------//--------------------------------------------
