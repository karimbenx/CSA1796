from heapq import heappush, heappop

def astar(start, goal, neighbors, heuristic):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        current_cost, current_node = heappop(open_list)
        
        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            return path[::-1]
        
        for neighbor in neighbors(current_node):
            new_cost = g_score[current_node] + heuristic(current_node, neighbor)
            
            if neighbor not in g_score or new_cost < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = new_cost
                heappush(open_list, (new_cost + heuristic(neighbor, goal), neighbor))
                
    return None

# Usage example
start, goal = (0, 0), (4, 4)

def neighbors(node):
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Defining neighbor positions

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance as heuristic

path = astar(start, goal, neighbors, heuristic)
print(f"Shortest path from {start} to {goal}: {path}")
