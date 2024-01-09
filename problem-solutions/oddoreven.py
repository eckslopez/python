# Check odd, even, multiple of 4
number = int(input("Enter a number:\n"))
if number%4 == 0:
    print("Even and a multiple of four.")
elif number%2 == 0:
    print("Even")
elif number%2 != 0:
    print("Odd")


