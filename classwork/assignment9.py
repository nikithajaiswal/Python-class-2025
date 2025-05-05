import string
from collections import Counter

# Input paragraph
text = "Hello world! Hello user. Python is fun. Python is great. Python is cool."

# Remove punctuation and convert to lowercase
clean_text = text.translate(str.maketrans('', '', string.punctuation)).lower()

#Split into words
words = clean_text.split()

# Count frequency using a dictionary (Counter is a handy dict subclass)
word_freq = Counter(words)

# Sort and get the top 5 most common words
top_5 = word_freq.most_common(5)

# Display the results
print("Top 5 most frequent words:")
for word, freq in top_5:
    print(f"{word}: {freq}")

