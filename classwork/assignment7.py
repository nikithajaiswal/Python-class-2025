import re
from collections import Counter

def calculate_similarity(doc1, doc2):
    # Clean both texts (remove punctuation, convert to lowercase)
    doc1 = re.sub(r'[^\w\s]', '', doc1).lower()
    doc2 = re.sub(r'[^\w\s]', '', doc2).lower()

    # Split into words and convert each to a set
    words1 = set(doc1.split())
    words2 = set(doc2.split())

    # Calculate total unique words in each
    total_unique_words1 = len(words1)
    total_unique_words2 = len(words2)

    # Calculate number of common words
    common_words = words1.intersection(words2)
    num_common_words = len(common_words)

    # Calculate percentage similarity based on intersection over union
    union = words1.union(words2)
    similarity = (num_common_words / len(union)) * 100

    return {
        'common_words': common_words,
        'similarity': f'{similarity:.2f}%'
    }

doc1 = "Machine learning is super powerful and useful."
doc2 = "Learning machines is very useful in data science."

result = calculate_similarity(doc1, doc2)
print(f"Common Words: {result['common_words']}")
print(f"Similarity: {result['similarity']}")

