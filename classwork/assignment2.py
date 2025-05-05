# Prime Number Checker

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Main program loop for multiple inputs
print("Enter a number to check if it's prime (or type 'q' to quit):")

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'q':
        break

    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    number = int(user_input)
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
