temperature = int(input("What's the temperature where you're at?\n"))
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

forecast = input("what's the forecast where you're at?\n")
if not forecast == "rainy":
    print("Go outside!")
else:
    print("Stay inside!")