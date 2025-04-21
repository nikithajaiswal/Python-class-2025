# 1. What are the standard data types in Python?  

# Ans:  Text type, numeric type, sequence type, set type, mapping type, Boolean type. 

# 2. What is the difference between mutable and immutable data types? Give examples.  

# In the mutable data type items within the variable can be changed, For example LIST, Datatype Dictionary. 

 # a = ['apple','orange','banana','kiwi','grapes'] 
# a[2]= 'cherry' ### it change the item to cherry  
# print(a)     ####output a = ['apple','orange',cherry,'kiwi','grapes'] 

# In the immutable date type items can not be changed, for example Tuple, set, string.

# a = ('apple','orange','banana','kiwi','grapes')
# a[2]= 'cherry'   
# print(a)  OUTPUT##TypeError: 'tuple' object does not support item assignment


# 3. What is the difference between a list and a tuple?  
#List are ordered, changeable, and allow duplicates and it is enclosed with [] square brackets
# Tuples are unordered, unchangeable and allow Duplicates and it is enclosed with () round brackets


# 4. How do you define a dictionary in Python?
# In Dictionary items are ordered, changeable and do not allow duplicates, It is a keys and value pair and it is enclosed in {} flower brackets


# 5. What is the difference between int and float data types? 
# int(integer) is all the whole numbers eg: (1,2,3,-4)
# # Float is the all the decimal numbers eg: (1.2,8.1, -10.0)

# 6. What is the output of type(10) and type(10.0)?  
# a =(type(10))
# print(a) 
# OUTPUT##<class 'int'>
# a=(type(10.0))
# print(a) ###OUTPUT<class 'float'>

# 7. What is the difference between is and == in Python?  
#  == in python compares the two values if they are equal to each other.

# 8. How do you convert one data type to another in Python? Give an example.  
#  we can convert one data type to another by converting iterables eg: Tuples 
# As tuples are unchangeable we can convert into list and make changes 
# example
# a = ('apple','orange','banana','kiwi','grapes')
# b =list(a)
# b.append('Python')
# a=tuple(b)
# print (b)

# 9. How do you check the data type of a variable in Python?  
# Data type can be checked by using type()function. For example
# a=(type(10.0))
# print(a) ###OUTPUT<class 'float'>
# a=(type('apple'))
# print(a) OUTPUT <class 'str'>

# 10. What is a set in Python? How is it different from a list? 
# SET items are unordered, Unchangeable and do not allow duplicates and it is enclosed within{}. 
# But in LIST items are in ordered, changeable and does allow duplicates and it is enclosed in []


# 11. Can you store different data types in a Python list?  
#  Yes. We can store different data types in python list 
# a =['abc',123,1.23,True]
# print(a)

# 12. What is type casting? How does it work in Python? 
#  Type casting is used to convert the variable from on data type to another datatype by creating a new variable.
# a = 10
# b = float(a)
# print(b)

# 13. What happens when you add an int and a str in Python?  
# If we add an int and a str in python it will print error TypeError: can only concatenate str (not "int") to str. We can not add int and str directly 
# a = "hello"+ 123
# print(a) 

# 14. What is a list in Python?  
#  LIST items are in ordered, changeable and does allow duplicates and it is enclosed in []

# 15. How do you create a list in Python? Give an example.  
# a =['apple','orange','banana','kiwi','grapes']
# print(a)

# 16. How do you access elements in a list using indexing?  
# a =['apple','orange','banana','kiwi','grapes']
# print(a[1])


# 17. What is negative indexing in lists? Give an example. 
#  Negative indexing allows to access the items from the end from right to left.  
# The  value -1 refers to the last index in a list, the value -2 refers to the last second.
# example:
# a =['apple','orange','banana','kiwi','grapes']
# print(a[-1])

# 18. How do you add elements to a list? Explain append(), extend(), and insert().  
# append() is used to add the item But it will only add the item at the end of the items
# a =['apple','orange','banana','kiwi','grapes']
# a.append('python')
# print(a)
# Extend() is used to extend one variable to another eg:
# a =['apple','orange','banana','kiwi','grapes']
# b =[1,2,3,4]
# a.extend(b)
# print(a)
# Insert() is used to add item at specified location
# a =['apple','orange','banana','kiwi','grapes']
# a.insert(3,'python')
# print(a)
# 19. How do you remove elements from a list? Explain remove(), pop(), and del.  
# remove() can be used to remove a specfic item
# a =['apple','orange','banana','kiwi','grapes']
# a.remove('apple')
# print(a)
# pop() can to be used to remove the item by index number, If no index number is entered by default last item will be removed.
# a =['apple','orange','banana','kiwi','grapes']
# a.pop(2)
# print(a)
# del it will delete entire code 
# a =['apple','orange','banana','kiwi','grapes']
# del a
# print(a)
# 20. What happens if you try to access an index that is out of range?  
# if you try to access an index that is out of range it will print error
# a =['apple','orange','banana','kiwi','grapes']
# print(a[5]) ##output IndexError: list index out of range
# 21. How do you reverse a list in Python?
# a =['apple','orange','banana','kiwi','grapes']
# # a.reverse()
# print(a)

# 22. How do you find the index of an element in a list?  
# You can find the index of an element in a list using the list.index() method.

# 23. How do you iterate through a list using a for loop?  
# a =['apple','orange','banana','kiwi','grapes']
# for i in a:
#     print(i)

# 24. What is the syntax of an if statement in Python? 
# if condition: 

# . How does the if-else statement work? Give an example.  
# if the given condition is not true it will print else statement
# a =22
# b=100
# if a<b:
#     print('Less than')
# else:
#     print('greater than')
# 26. What is the role of the elif statement?  
# elif statement is used to text multiple conditions 
# It provides another condition that is checked only if all of the previous conditions were False.

# 27. How do you check if a number is divisible by both 3 and 5 using if-else?  
# a = int(input("Enter a number: "))

# if a % 3 == 0 and a % 5 == 0:
#     print("Divisble")  
# else:
#     print("Not divisible by both.")

# 28. Write a Python program to check whether a person is eligible to vote (age ≥ 18).

# age = int(input("Enter your age: ")) 

# if age >= 18:
#     print("You are eligible to vote!")
# else:
#     print(f"Not Eligible. Wait for {18 - age} more years.")

# 29. What happens if you don’t use indentation properly in an if-else statement?  
#  if we dont use indentation properly it will give error : ndentationError: expected an indented block after 'else' statement on line 173

# 30. Write a Python program to compare two numbers and print the larger one.  
# Input two numbers
# num1 = int(input("Enter the first number: "))  
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print(f"The larger number is: {num1}")
# elif num2 > num1:
#     print(f"The larger number is: {num2}")
# else:
#     print("Both numbers are equal.")
# 31. How can you use an if statement without an else?  
# a = 44
# b= 100
# if a<b:
#     print('a is less than b')

# 32. Write a program to check if a given year is a leap year or not. 
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.") 

# 33. How do you use a nested if statement? Provide an example
# A nested if is an if statement inside another if/else block. 
# a = 44
# b = 500
# if a<b:
#     print('one')
#     if a==b:
#         print('two')
#     else:
#         print(False)
# else:
#     print('no')        
   

# 34. Write a program to check if a character is a vowel or consonant  
# vow = input("Enter a character: ")
# if len(vow) == 1:
#    if vow in 'aeiouAEIOU':
#        print("Entered character is a vowel")
#    else:
#        print("Entered character is a consonant")
# else:
#    print("Enter a single character")

# 35. How can you check if a given number is within a specific range (e.g., 10-50)? 
# num = 40
# if num in range(10, 51):  # 51 because range() is exclusive
#     print(f"{num} is in range.")
# else:
#     print(f"{num} is out of range.")