a = []
number = int(input("Enter a number:\n"))
# Setting up the range tricked me. Not the programming
# concept, but the math concept. I thought all I need to test
# were the numbers 1-9 or 10, instead of 1-number.
for i in list(range(1,number+1)):
    if number%i == 0:
        a.append(i)
print(a)
