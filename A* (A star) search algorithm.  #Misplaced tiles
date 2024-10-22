import heapq
import numpy as np

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return (i, j)

# Heuristic: Misplaced tiles
def misplaced_tiles(state, goal_state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j] and state[i][j] != 0)

def is_goal(state, goal_state):
    return np.array_equal(state, goal_state)

def print_state(state):
    for row in state:
        print(row)
    print()

def get_neighbors(node):
    neighbors = []
    x, y = find_blank(node.state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = np.copy(node.state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star_search(start_state, goal_state):
    open_list = []
    closed_set = set()

    start_node = Node(state=start_state, g=0, h=misplaced_tiles(start_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if is_goal(current_node.state, goal_state):
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor in get_neighbors(current_node):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple in closed_set:
                continue

            g = current_node.g + 1
            h = misplaced_tiles(neighbor, goal_state)
            neighbor_node = Node(state=neighbor, parent=current_node, g=g, h=h)

            heapq.heappush(open_list, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def input_state(prompt):
    while True:
        try:
            print(prompt)
            state = list(map(int, input().split()))
            if len(state) != 9 or set(state) != set(range(9)):
                raise ValueError("Input must be 9 numbers from 0 to 8 with no duplicates.")
            return np.array(state).reshape((3, 3))
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

if __name__ == "__main__":
    start_state = input_state("Enter the start state (9 numbers, 0 for blank):")
    goal_state = input_state("Enter the goal state (9 numbers, 0 for blank):")

    print("Using Misplaced Tiles Heuristic:")
    solve_puzzle(start_state, goal_state)
