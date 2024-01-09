import datetime

def main():
    name = input("Please enter your name.\n")
    age = int(input("Now please enter your age\n"))

    # Get the current year
    today = datetime.date.today()
    this_year = today.year

    # How many years until user turns 100
    years_to_onehundred = 100 - age
    # Get the year they turn 100
    year_centenarian =  this_year + years_to_onehundred


    print(name + ", you will be 100 years old in the year " + str(year_centenarian) + ".")

main()