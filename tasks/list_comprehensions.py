# Create a new list from another list:
years_of_birth = [1990,1992,1990,1992,1991]
ages = []
for year in years_of_birth:
    ages.append(2023 - year)
print(ages)

# A more compact version, using comprehensions:
years_of_birth = [1990,1992,1990,1992,1991]
ages = [2023 - year for year in years_of_birth]
print(ages)

# Another example:
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# An equivalent example:
squares = list(map(lambda x: x**2,range(10)))

# Another equivalent example:

squares = [x**2 for x in range(10)]