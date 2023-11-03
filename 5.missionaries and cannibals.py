from collections import deque

def valid(state):
    m, c, b = state
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m < c and m > 0:
        return False
    if 3 - m < 3 - c and 3 - m > 0:
        return False
    return True

def solve():
    start = (3, 3, 1)  # (missionaries, cannibals, boat position)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        visited.add(state)
        m, c, b = state

        for d_m in range(3 + 1):  # Maximum 3 missionaries
            for d_c in range(3 + 1):  # Maximum 3 cannibals
                if 0 < d_m + d_c <= 2:  # Boat capacity: maximum of 2 people
                    new_state = (m - d_m * b, c - d_c * b, 1 - b)
                    if valid(new_state) and new_state not in visited:
                        queue.append((new_state, path + [new_state]))

    return None

solution = solve()
if solution:
    print("Solution found in", len(solution) - 1, "steps:")  # Adjusted to exclude initial state
    for step in solution:
        print(step)
else:
    print("No solution found.")
