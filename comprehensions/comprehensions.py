from math import factorial
from math import sqrt
from pprint import pprint as pp

# Comprehensions:
# Concise syntax for describing lists, sets, and dictionaries.

# List Comprehension Syntax
# [ expr(item) for item in iterable]

# Example: Calculate the length of each word and return a 
# newly constructed list. 
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print([len(word) for word in words])

# The Comprehension is the DECLARATIVE equivalent of the following
# IMPERATIVE code:
lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)
    
# Set Comprehensions
s = {len(str(factorial(x))) for x in range(20)}
type(s)
print(s)

# Dictionary Comprehensions
country_to_capital = { 'United Kingdon': 'London',
                       'Brazil': 'Brasilia',
                       'Morocco': 'Rabat',
                       'Sweden': 'Stockholm'}

# Invert the keys and values
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

# Filtering Comprehensions
def is_prime(x):
    




#print("Here's an example of a multi input comprehension.")
#grid = [(x,y) for x in range(5) for y in range(5)]
#print(grid)

#print("Here's an example of the equivalent using a nested for-loop")
#points = []
#for x in range(5):
#    for y in range(5):
#        points.append((x,y))
#print(points)