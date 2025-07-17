class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Function to insert a node
def insert_node(parent_map, root, u, v, direction):
    if u not in parent_map:
        parent_map[u] = Node(u)
    if v not in parent_map:
        parent_map[v] = Node(v)
        
    if direction == 'l':
        parent_map[u].left = parent_map[v]
    else:
        parent_map[u].right = parent_map[v]
        
    if root[0] is None:
        root[0] = parent_map[u]

# Function to check mirror
def are_mirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.data == t2.data and 
            are_mirror(t1.left, t2.right) and 
            are_mirror(t1.right, t2.left))

# Main
n = int(input())

# Tree 1
tree1_map = {}
root1 = [None]
for _ in range(n):
    u, v, d = input().split()
    insert_node(tree1_map, root1, int(u), int(v), d)

# Tree 2
tree2_map = {}
root2 = [None]
for _ in range(n):
    u, v, d = input().split()
    insert_node(tree2_map, root2, int(u), int(v), d)

# Check for mirror
if are_mirror(root1[0], root2[0]):
    print("Yes, the trees are mirrors of each other.")
else:
    print("No, the trees are not mirrors.")
