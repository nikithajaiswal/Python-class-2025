text = input()  # Read the input string
hist = {}       # Create an empty dictionary

# Count each letter
for letter in text:
    if letter in hist:
        hist[letter] += 1
    else:
        hist[letter] = 1

# Sort and print the result
for letter in sorted(hist):
    print("Letter", letter, " appears ", hist[letter], " time/s")