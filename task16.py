# Take input from the user for the filename
filename = input()

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
        # Split content into words using split()
        words = content.split()
        # Print the number of words
        print(len(words))
except FileNotFoundError:
    print("File not found.")
