from itertools import groupby

# Read input string from STDIN
S = input()

# Apply groupby to count consecutive characters
result = []
for key, group in groupby(S):
    count = len(list(group))
    result.append(f"({count}, {key})")

# Print the result as a single string
print(' '.join(result))
