import random

players = ['Xavier Lopez',
           'Mike Douglas', 
           'Paul Hourani', 
           'Marvin Artavia', 
           'Rafael Wuence', 
           'Mike Le', 
           'Jose Rangel',
           'Josh Cameron',
           'Ricardo Reta']

# Shuffle the list
random.shuffle(players)

# Print the shuffled list
for item in players:
    print(item)