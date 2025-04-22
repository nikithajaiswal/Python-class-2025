def grade_book_system():
    grades = {
        'John': [80, 85, 90],
        'Sara': [70, 75, 78]
    }

    # Task 1: Add a new student with scores
    def add_student(name, scores):
        grades[name] = scores

    # Task 2: Add scores for an existing student
    def add_scores(name, scores):
        if name in grades:
            grades[name].extend(scores)
        else:
            print("Student not found")

    # Task 3: Calculate average score for each student
    def calculate_average():
        averages = {}
        for name, scores in grades.items():
            average = sum(scores) / len(scores)
            averages[name] = average
        return averages

    # Task 4: Identify students with the highest and lowest average
    def find_top_and_lowest(averages):
        top_student = max(averages, key=averages.get)
        lowest_student = min(averages, key=averages.get)
        return top_student, lowest_student

    # Add a new student with scores
    add_student('Emily', [90, 92, 88])

    # Add scores for an existing student
    add_scores('John', [95, 98])

    # Calculate average score for each student
    averages = calculate_average()

    # Identify students with the highest and lowest average
    top_student, lowest_student = find_top_and_lowest(averages)

    # Print results
    for name, average in averages.items():
        print(f"Average for {name}: {average:.1f}")
    print(f"Top student: {top_student}")
    print(f"Lowest scoring student: {lowest_student}")

grade_book_system()