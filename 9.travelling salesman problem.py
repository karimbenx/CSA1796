from itertools import permutations

# Get the number of cities from the user
num_cities = int(input("Enter the number of cities: "))

# Initialize an empty list to store distances
distances = []

# Get distances between cities from the user
print("Enter the distances between the cities:")
for i in range(num_cities):
    distances.append(list(map(int, input().split())))

min_distance = float('inf')
best_route = None

for route in permutations(range(num_cities)):
    distance = sum(distances[route[i % num_cities]][route[(i + 1) % num_cities]] for i in range(num_cities))
    if distance < min_distance:
        min_distance = distance
        best_route = route

print(f"The shortest route is: {best_route} with a distance of {min_distance}.")
