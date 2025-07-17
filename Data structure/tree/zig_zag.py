class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Build the tree from edge list
def build_tree(n, edge_list):
    nodes = {}
    for edge in edge_list:
        u, v, c = edge
        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)
        if c == 'L':
            nodes[u].left = nodes[v]
        elif c == 'R':
            nodes[u].right = nodes[v]
    return nodes[edge_list[0][0]]  # return the root node

# Zigzag level-order traversal
def zigzag_traversal(root):
    if root is None:
        return

    current_level = [root]
    left_to_right = True
    result = []

    while current_level:
        level_values = [0] * len(current_level)
        next_level = []

        for i in range(len(current_level)):
            node = current_level[i]
            index = i if left_to_right else len(current_level) - 1 - i
            level_values[index] = node.data
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.extend(level_values)
        current_level = next_level
        left_to_right = not left_to_right

    print(" ".join(str(x) for x in result))

# Input and function call
n = int(input())
edges = []
for _ in range(n - 1):
u, v, c = input().split()
edges.append((int(u), int(v), c))
root = build_tree(n, edges)
zigzag_traversal(root)