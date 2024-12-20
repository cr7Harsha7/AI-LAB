# Alpha-Beta Pruning Implementation

# Function to evaluate a leaf node (example heuristic function)
def evaluate(node):
    return node  # For leaf nodes, the value itself is returned

# Alpha-Beta Pruning Function
def alphaBeta(node, depth, alpha, beta, isMaximizer, tree, path=[]):
    # Base case: if we reach a leaf node or maximum depth
    if depth == 0 or not isinstance(node, list):
        print(f"Leaf Node {node} -> Returning: {evaluate(node)}")
        return evaluate(node)
    
    if isMaximizer:
        value = float('-inf')  # Initialize value to negative infinity
        print(f"Maximizer at Node {path}, Alpha: {alpha}, Beta: {beta}")
        for i, child in enumerate(node):  # Traverse all children
            value = max(value, alphaBeta(child, depth-1, alpha, beta, False, tree, path + [i]))
            alpha = max(alpha, value)  # Update alpha
            print(f"Maximizer Updated Alpha: {alpha} at Node {path + [i]}")
            if alpha >= beta:  # Pruning condition
                print(f"Pruning at Node {path + [i]} (Alpha: {alpha} >= Beta: {beta})")
                break  # Prune remaining branches
        return value
    else:
        value = float('inf')  # Initialize value to positive infinity
        print(f"Minimizer at Node {path}, Alpha: {alpha}, Beta: {beta}")
        for i, child in enumerate(node):  # Traverse all children
            value = min(value, alphaBeta(child, depth-1, alpha, beta, True, tree, path + [i]))
            beta = min(beta, value)  # Update beta
            print(f"Minimizer Updated Beta: {beta} at Node {path + [i]}")
            if alpha >= beta:  # Pruning condition
                print(f"Pruning at Node {path + [i]} (Alpha: {alpha} >= Beta: {beta})")
                break  # Prune remaining branches
        return value

# Example Game Tree
# Depth-4 Tree: Leaves at depth 0
tree = [
    [  # Level 1: Left Subtree
        [10, 9],  # Level 2: Left Child of Left Subtree
        [14, 18]  # Level 2: Right Child of Left Subtree
    ],
    [  # Level 1: Right Subtree
        [5, 4],   # Level 2: Left Child of Right Subtree
        [50, 3]   # Level 2: Right Child of Right Subtree
    ]
]

# Root Node (MAX's turn)
depth = 4
alpha = float('-inf')
beta = float('inf')

# Start Alpha-Beta Pruning
best_value = alphaBeta(tree, depth, alpha, beta, True, tree)

print("\nBest Value for Root Node:", best_value)
