# Take a list, say for for example this one:
# a = [1,1,2,3,5,8,13,21,34,55,89]
# and write a program that prints out all the elements 
# of the list that are less than 5.

# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#     if i < 5:
#         print(i)

# Extras:
# 1. Instead of printing the elements one by one, make a new list that
#    has all the elements less than 5 and print out the new list.

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i) 

# print(b)

# 2. Write this in one line of Python

# 3. Ask the user for a number and return a list that contains only elements
#    from the original list that are smaller than that number.

a = [1,1,2,3,5,8,13,21,34,55,89]
number = int(input("Enter a number:\n"))
for i in a:
    if i < number:
        print(i)

