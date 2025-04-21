# # create a 3 functions, use the 1st function in the 2nd function, use the 2nd function in the 3rd
# def abc():
#     a = 3
#     b= 3
#     print(a+b)
# abc()

# def bcd():
#     abc()
#     c= 4
#     print(c)
# bcd()

# def efg():
#     bcd()
#     d= 17
#     print(d)

# efg()
    
# create a 2 global variables, create 4 functions, create 4 local variables, call al the different function in each other

# a =2
# b= 45
# def ccc():
#     c =4
#     print(a+c)
# ccc()

# def eee():
#     d = 1
#     print(d+b)
# eee()

# def fff():
#     e = 6
#     print(e+a)
# fff()
# def egh():
#     f = 10
#     print(a*f)
# egh()

# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
# if num1> num2:
#     print(f"The greater number is {num1}: ")
# elif num2> num1:
#     print(f"The greater number is {num2}:")
# else:
#     print("Both are equal")
    
# integer_var: int = 10.2
# # x:int 
# # integer_var = 10.20
# # print(type(integer_var))

# print(integer_var)

# str = 'abs'
# print(str)

# print(type(10))
# print(isinstance("abc",float))
# print(10,20,30,40, sep=" ---- ")
# x, y = input("Enter two numbers (separated by space): ").split()
# x = int(x)
# y = int(y)
# print(f"Sum: {x + y}")

# def greet(name):  
#     print(f"Hello, {name}!")

# greet("Alice")  
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)

# print(factorial(5)) 

# a= ('apple', 'orange', 'banana','apple')
# b= list(a)
# b.sort()
# a=tuple(b)
# print(a)


# b= {'apple', 'orange', 'banana','apple'}
# b.sort()
# print(b)

# print(type(int('123')))
# a = 'abc'
# print(type(a))


# def abc(a,b):
#     return a+b
# print(abc(1,2))

# def factorical(n):
#     if n == 1:
#         return 1
#     return n * factorical(n-1)
# print(factorical(5))

# def greet(name= "nikitha"):
#     print(f"hello {name}")

# greet('sai')

# def total(*numbers):
#     # print(numbers)
#     return sum(numbers)

# print(total(1, 2, 3, 4))  # Output: 10
# lst = [1, 2, 3]
# lst.append([4, 5])
# print(len(lst))

# # Given a string:
# sentence = "Learning Python is FUN!"

# # Convert it to:
# # - all lowercase
# print(sentence.lower())
# # - all uppercase
# print(sentence.upper())


text = "apple banana cherry"

# a. Split the string into a list
print(text.split())
# b. Join the list using a comma and print the result
# print(",".join(text.split()))