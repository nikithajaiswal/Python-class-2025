# a. String Basics, String Indexing & Slicing, len()
# String Basics

# In Python, a string is a sequence of characters enclosed in quotes (single, double, or triple quotes). 
# Strings are immutable, meaning they cannot be changed after creation.

# String Indexing

# String indexing allows you to access individual characters in a string. 
# Indexing starts at 0, meaning the first character is at index 0.

# my_string = "Hello"
# print(my_string[0])  # Output: H
# print(my_string[4])  # Output: o
# String Slicing

# String slicing allows you to extract a subset of characters from a string. The syntax is my_string[start:stop:step].

# start: The starting index (inclusive).
# stop: The ending index (exclusive).
# step: The increment between indices (default is 1).
# python
# CopyInsert
# my_string = "Hello"
# print(my_string[1:3])  # Output: el
# print(my_string[1:])  # Output: ello
# print(my_string[:3])  # Output: Hel
# print(my_string[::2])  # Output: Hlo
# len()

# The len() function returns the length of a string.

# python
# CopyInsert
# my_string = "Hello"
# print(len(my_string))  # Output: 5
# b. String Methods
# upper()

# The upper() method returns a copy of the string in uppercase.

# python
# CopyInsert
# my_string = "hello"
# print(my_string.upper())  # Output: HELLO
# lower()

# The lower() method returns a copy of the string in lowercase.

# python
# CopyInsert
# my_string = "HELLO"
# print(my_string.lower())  # Output: hello
# strip()

# The strip() method removes leading and trailing whitespace from the string.

# python
# CopyInsert
# my_string = "   hello   "
# print(my_string.strip())  # Output: hello
# find()

# The find() method returns the index of the first occurrence of a substring. If not found, it returns -1.

# python
# CopyInsert
# my_string = "hello world"
# print(my_string.find("world"))  # Output: 6
# print(my_string.find("foo"))  # Output: -1
# replace()

# The replace() method replaces all occurrences of a substring with another substring.

# python
# CopyInsert
# my_string = "hello world"
# print(my_string.replace("world", "python"))  # Output: hello python
# split()

# The split() method splits the string into a list of substrings based on a separator.

# python
# CopyInsert
# my_string = "hello world"
# print(my_string.split())  # Output: ['hello', 'world']
# print(my_string.split(" "))  # Output: ['hello', 'world']
# join()

# The join() method concatenates a list of strings into a single string using a separator.

# python
# CopyInsert
# my_list = ["hello", "world"]
# print(" ".join(my_list))  # Output: hello world
# These are the basic string manipulation methods in Python. I hope this explanation helps!

text = "hello"

for i in range(len(text)):
    print(f"Character at index {i} is {text[i]}")

