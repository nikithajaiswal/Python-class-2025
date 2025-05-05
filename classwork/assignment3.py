# Student Scores Program

students = {}

# Collect data for 5 students
for i in range(5):
    name = input(f"Enter student name ({i+1}/5): ")
    while True:
        try:
            score = float(input(f"Enter score for {name}: "))
            break
        except ValueError:
            print("Invalid score. Please enter a numeric value.")
    students[name] = score

# Calculate average
average_score = sum(students.values()) / len(students)

# Find highest and lowest scorers
highest_scorer = max(students, key=students.get)
lowest_scorer = min(students, key=students.get)

# Display results
print("\n--- Results ---")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Scorer: {highest_scorer} with {students[highest_scorer]}")
print(f"Lowest Scorer: {lowest_scorer} with {students[lowest_scorer]}")
