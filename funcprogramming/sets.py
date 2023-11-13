blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Jack', 'Amelia'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
print(blue_eyes.intersection(blond_hair))
