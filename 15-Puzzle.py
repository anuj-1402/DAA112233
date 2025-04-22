import heapq
import copy

# Final goal state of 15 puzzle
goal_state = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

# Direction vectors for up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Puzzle Node structure
class PuzzleNode:
    def __init__(self, mat, x, y, level, parent):
        self.mat = mat
        self.x = x
        self.y = y
        self.level = level
        self.parent = parent
        self.heuristic = self.calculate_heuristic()
        self.cost = self.level + self.heuristic  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_heuristic(self):
        # Manhattan distance as heuristic
        h = 0
        for i in range(4):
            for j in range(4):
                val = self.mat[i][j]
                if val != 0:
                    goal_x = (val - 1) // 4
                    goal_y = (val - 1) % 4
                    h += abs(i - goal_x) + abs(j - goal_y)
        return h

# Check if position is within bounds
def is_valid(x, y):
    return 0 <= x < 4 and 0 <= y < 4

# Print a 4x4 matrix
def print_matrix(mat):
    for row in mat:
        print(row)
    print()

# Print the solution path from initial state to goal
def print_solution_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()

    print("\n===== Final solution path =====\n")
    for i, step in enumerate(path):
        print(f"Step {i}: g = {step.level}, h = {step.heuristic}, f = {step.cost}")
        print_matrix(step.mat)

# Branch and Bound Solver
def solve_15_puzzle(initial_state):
    # Locate blank (0) position
    x, y = next((i, j) for i in range(4) for j in range(4) if initial_state[i][j] == 0)

    root = PuzzleNode(initial_state, x, y, 0, None)

    pq = []
    heapq.heappush(pq, root)

    visited = set()
    step_count = 0

    print("===== Exploring nodes =====\n")

    while pq:
        current = heapq.heappop(pq)
        step_count += 1

        print(f"Node {step_count}: g = {current.level}, h = {current.heuristic}, f = {current.cost}")
        print_matrix(current.mat)

        if current.mat == goal_state:
            print("\n===== Solution found =====")
            print_solution_path(current)
            print(f"Total nodes expanded: {step_count}")
            print(f"Total moves to reach solution: {current.level}")
            return

        visited.add(str(current.mat))

        for dir in range(4):
            new_x = current.x + dx[dir]
            new_y = current.y + dy[dir]

            if is_valid(new_x, new_y):
                new_mat = copy.deepcopy(current.mat)
                new_mat[current.x][current.y], new_mat[new_x][new_y] = new_mat[new_x][new_y], new_mat[current.x][current.y]

                if str(new_mat) not in visited:
                    child = PuzzleNode(new_mat, new_x, new_y, current.level + 1, current)
                    heapq.heappush(pq, child)

# Sample input
initial_state = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 10, 7, 12],
    [13, 14, 11, 15]
]

solve_15_puzzle(initial_state)
