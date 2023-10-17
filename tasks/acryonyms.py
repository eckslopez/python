def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")
    found = False

    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
        if not found:
            print("The acronym doesn't exist.")

def add_acronym():
    acronym = input("Which acronym would you like to add?\n")
    definition = input("What is the definition of the acronym?\n")

    with open('acronyms.txt', 'a', encoding="utf-8") as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find or add an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()