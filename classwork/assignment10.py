import math

# Input: list of 2D points
points = [(1, 2), (4, 6), (5, 9), (9, 9)]

# List to store distances between each pair
distances = []

# Loop to calculate distance between each pair of points
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distances.append(distance)
    print(f"Distance between {points[i]} and {points[i + 1]}: {distance:.1f}")

# Total path length
total_path = sum(distances)
print(f"Total Path Length: {total_path:.1f}")
