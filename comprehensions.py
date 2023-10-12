# [ expr(item) for item in iterable]
# Example: 

words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print([len(word) for word in words])

#print("Here's an example of a multi input comprehension.")
#grid = [(x,y) for x in range(5) for y in range(5)]
#print(grid)

#print("Here's an example of the equivalent using a nested for-loop")
#points = []
#for x in range(5):
#    for y in range(5):
#        points.append((x,y))
#print(points)