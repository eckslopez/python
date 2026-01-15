# 1. Read the file line-by-line
# 2. Parse each line for the direction and distance: L is subtraction, R is addition, the number is the distance. The
#    rotation direction can be found by parsing for the first character of the string. The distance can be found by
#    parsing from the second character, to the end of the string.
# 3. Location starts at 50.
# 4. Subsequent locations are calculated by (subtracting the distance) % 100, (adding the distance) %100.
# 5. If the new location, calculated in #4 == 0, increment a counter. We'll call it 'zeroes'.
# 6. The counter will have the count of zeroes.

file_path = 'turns.txt'

# Read file line-by-line
with open(file_path, 'r') as rotations:
    # Set the initial position
    position = 50
    # Set a zero counter to increment
    zeroes = 0 

    # Read the file line-by-line
    for r in rotations:
        # Set the distance as all characters following the first character
        distance = r[1:]
        # Convert the distance to an integer
        distance = int(distance)
        # Read the first character
        if r[0] == 'L':
            new_position = (position - distance) % 100
        else:
            new_position = (position + distance) % 100
        
        # Set the position equal to the new_position, which was just
        # calculated, for the next line in the file
        position = new_position 

        # Increment the zero counter, if the position == 0 
        if position == 0: zeroes += 1
        
    print(zeroes)
