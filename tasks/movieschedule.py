current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print("We're currently showing the following movies:\n")
for key in current_movies:
    print(key)

movie = input("\nWhat movie would you like the showtime for?\n")
showtime = current_movies.get(movie)

if showtime == None:
    print("\nThat movie is not playing today.\n")
else:
    print("\nGreat choice! You can see " + movie + " at " + current_movies.get(movie) + ".")
