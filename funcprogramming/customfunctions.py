#def greeting(name):
#    print('Hello', name)

# Main program 
#input_name = input('Enter your name:\n')

#greeting(input_name)

#def addition(a, b):
#    return a + b 

# Main program 
#num1 = float(input('Enter you 1st number:\n'))
#num2 = float(input('Enter you 2nd number:\n'))

#result = addition(num1, num2)
#print('The result is ', result)

def booyah(w1,w2,w3):
    return str(w1 + ' ' + w2 + ' ' + w3)

w1 = input("Let's make a sentence. Enter a word:\n")
w2 = input("Enter another word:\n")
w3 = input("Enter one more word:\n")

sentence = booyah(w1,w2,w3)
print(sentence)