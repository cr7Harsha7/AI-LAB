import random
import math

def create_board(n, initial_config=None):
    """Create a board with the specified initial configuration."""
    if initial_config:
        return initial_config  # Use the provided initial configuration
    return [random.randint(0, n-1) for _ in range(n)]

def count_conflicts(board):
    """Count the number of pairs of queens that are attacking each other."""
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(board):
    """Generate neighbors by moving one queen at a time to a different row."""
    neighbors = []
    for i in range(len(board)):
        for row in range(len(board)):
            if row != board[i]:
                neighbor = board[:]
                neighbor[i] = row
                neighbors.append(neighbor)
    return neighbors

def print_board(board):
    """Print the board in a human-readable format."""
    n = len(board)
    for row in range(n):
        line = ['Q' if board[col] == row else '.' for col in range(n)]
        print(' '.join(line))
    print()

def simulated_annealing(n, initial_config, max_iterations=1000, initial_temperature=100, cooling_rate=0.95):
    """Solve the N-Queens problem using simulated annealing."""
    current_board = create_board(n, initial_config)
    current_conflicts = count_conflicts(current_board)
    temperature = initial_temperature
    
    best_board = current_board[:]
    best_conflicts = current_conflicts
    
    # Print the initial configuration
    print("Initial configuration:")
    print_board(current_board)
    print(f"Initial number of conflicts: {current_conflicts}\n")
    
    for iteration in range(max_iterations):
        if current_conflicts == 0:
            # If the solution is found, print the final configuration and exit
            print(f"Solution found at iteration {iteration + 1}!")
            print("Final configuration (solution):")
            print_board(current_board)
            return current_board
        
        # Get neighbors of the current board
        neighbors = get_neighbors(current_board)
        next_board = random.choice(neighbors)
        next_conflicts = count_conflicts(next_board)
        
        # If the neighbor has fewer conflicts, accept it
        if next_conflicts < current_conflicts:
            current_board = next_board
            current_conflicts = next_conflicts
        else:
            # Accept the neighbor with a certain probability
            probability = math.exp((current_conflicts - next_conflicts) / temperature)
            if random.random() < probability:
                current_board = next_board
                current_conflicts = next_conflicts
        
        # Update temperature
        temperature *= cooling_rate
        
    # If no solution is found, print the best state after max iterations
    print(f"No solution found within {max_iterations} iterations.")
    print("Best configuration found:")
    print_board(best_board)
    return best_board

# Set the number of queens (4 for this example) and initial configuration
n = 4
initial_config = [2, 1, 3, 0]  # The custom configuration
solution = simulated_annealing(n, initial_config)
