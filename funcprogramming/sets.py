blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Jack', 'Amelia'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# All those with blue eyes, blond hair or both.
print(blue_eyes.union(blond_hair))
# Communtative
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
# All those with blond hair and blue eyes.
print(blue_eyes.intersection(blond_hair))
# Also commutative
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))
# Those with blond hair that don't have blue eyes.
print(blond_hair.difference(blue_eyes))
# Non-commutative
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))
# All the people who have exclusively blond hair or blue eyes,
# but not both.
print(blond_hair.symmetric_difference(blue_eyes))
# Commutative, as you can tell by the name.
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))
# Predicate methods that tell us about the relationships between sets.
# Check that all elements in the first set are present in the second set.
print(smell_hcn.issubset(blond_hair))
# Checks that all elements of the second set are present in the first set.
print(taste_ptc.issuperset(smell_hcn))
# Check that two sets have no members in common.
print(a_blood.isdisjoint(o_blood))
