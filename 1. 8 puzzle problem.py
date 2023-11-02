import copy
from heapq import heappush, heappop

n = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class Queue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

class node:
    def __init__(self, parent, mat, empty, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty = empty
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def CalculateCost(mat, final):
    count = 0
    for i in range(n):
        for j in range(n):
            if (mat[i][j] and (mat[i][j] != final[i][j])):
                count += 1
    return count

def newNode(mat, empty, new_empty, level, parent, final):
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty
    x2, y2 = new_empty
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = CalculateCost(new_mat, final)
    new_node = node(parent, new_mat, new_empty, cost, level)
    return new_node

def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end="")
        print()
    print()

def Valid(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def printPath(root):
    if root == None:
        return
    printPath(root.parent)
    printMatrix(root.mat)

def solve(initial, empty, final):
    pq = Queue()
    cost = CalculateCost(initial, final)
    root = node(None, initial, empty, cost, 0)
    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            printPath(minimum)
            return

        for i in range(4):
            new_tile = [minimum.empty[0] + row[i], minimum.empty[1] + col[i]]
            if Valid(new_tile[0], new_tile[1]):
                child = newNode(minimum.mat, minimum.empty, new_tile, minimum.level + 1, minimum, final)
                pq.push(child)

# Driver code
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty = [1, 2]

solve(initial, empty, final)
