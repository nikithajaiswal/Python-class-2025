# Recursive function to calculate factorial
# def factorial(n):
#     if n < 0:
#         return "Invalid input (negative number)"
#     if n == 0 or n == 1:  # base case
#         return 1
#     return n * factorial(n - 1)
# 5*4*3*2*1= 120

# Recursive function to calculate sum of first N natural numbers
def sum_natural(n):
    if n < 0:
        return "Invalid input (negative number)"
    if n == 0:  # base case
        return 0
    return n + sum_natural(n - 1)
# 5+4+3+2+1=15

# Main code
num = int(input("Enter a number: "))

# fact_result = factorial(num)
sum_result = sum_natural(num)

# print(f"Factorial of {num} is {fact_result}")
print(f"Sum of first {num} natural numbers is {sum_result}")
