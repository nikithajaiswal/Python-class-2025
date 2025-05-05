def add_employee(time_log, employee, hours=None):
    
    if employee not in time_log:
        time_log[employee] = hours if hours else []
    else:
        print(f"Employee '{employee}' already exists.")

def add_hours(time_log, employee, hours):
    
    if employee in time_log:
        time_log[employee].append(hours)
    else:
        print(f"Employee '{employee}' not found.")

def get_total_hours(time_log):
    
    total_hours = {}
    for employee, hours in time_log.items():
        total_hours[employee] = sum(hours)
    return total_hours

def find_most_hardworking(time_log):
    
    total_hours = get_total_hours(time_log)
    most_hardworking = max(total_hours, key=total_hours.get)
    return most_hardworking 

# Example usage:
time_log = {
    'Alice': [8, 9, 7],
    'Bob': [10, 5, 6]
}

add_employee(time_log, 'Charlie', [8, 4, 10])
add_hours(time_log, 'Alice', 10)
total_hours = get_total_hours(time_log)
most_hardworking = find_most_hardworking(time_log)

print("Total hours for each employee:")
for employee, hours in total_hours.items():
    print(f"{employee}: {hours}")

print(f"Most hardworking: {most_hardworking}")