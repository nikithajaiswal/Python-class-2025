# Arithmetic Operations Script

def perform_operations(a, b):
    # Perform calculations
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    # Handle division by zero
    if b != 0:
        division = a / b
        division_result = f"{a} / {b} = {division:.2f}"
    else:
        division_result = f"{a} / {b} = Error (Division by zero)"

    # Print results
    print(f"\nResults for inputs {a} and {b}:")
    print(f"{a} + {b} = {addition}")
    print(f"{a} - {b} = {subtraction}")
    print(f"{a} * {b} = {multiplication}")
    print(division_result)

# Main program loop for multiple inputs
print("Enter pairs of numbers separated by space (e.g., '2 4'). Type 'q' to quit.")
while True:
    user_input = input("Enter Two numbers: ")
    if user_input.lower() == 'q':
        break

    try:
        num1_str, num2_str = user_input.strip().split()
        num1 = float(num1_str)
        num2 = float(num2_str)
        perform_operations(num1, num2)
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")