from typing import List
from itertools import pairwise

def find_missing_numbers(sequence: List[int]) -> List[int]:
    """
    Given a list of integers that should be consecutive, 
    find all missing numbers in the sequence.
    
    The sequence starts at the minimum number and should go to the maximum.
    
    Explanation:
    - Range should be 1 to 9
    - Missing: 3, 5, 8
    """
    sequence = [1, 2, 4, 6, 7, 9]
    missing = []
    # Iterate through the list up to the second-to-last element
    for i in range(len(sequence) - 1):
        current_num = sequence[i]
        next_num = sequence[i+1]
        # Check if the next number is more than 1 greater than the current number
        if next_num - current_num > 1:
            # Add all the missing nums to the missing list
            for j in range(current_num + 1, next_num):
                missing.append(j)
    return missing

    
    #Should return: [3, 5, 8]


# Test
if __name__ == "__main__":
    sequence = [1, 2, 4, 6, 7, 9]
    result = find_missing_numbers(sequence)
    expected = [3, 5, 8]
    print(f"Missing numbers: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")