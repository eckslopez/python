# Ask the user which acronym they would like to add
# Ask the user for the definition.
# Open the file
# Write the acronym to the file.

acronym = input("Which acronym would you like to add?\n")
definition = input("What is the definition of the acronym?\n")

with open('acronyms.txt', 'a', encoding="utf-8") as file:
    file.write(acronym + ' - ' + definition + '\n')