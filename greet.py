import argparse

# Create parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--name',type=str,required=True)

# Parse the argument
args = parser.parse_args()

# Print "Hello" + the user input argument
print('Hi', args.name)