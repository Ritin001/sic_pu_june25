class node:
    def __init__(self,data=0):
        
        self.left = None
        self.data = data
        self.right = None
    
class BST:
    def __init__(self):
        self.root= None
        print("empty tree is created")
    
    def add_node(self,current_node,data):
        if current_node==None:
            return node(data)
        elif current_node.data > data:
            current_node.left = self.add_node(current_node.left,data)
        elif current_node.data < data:
            current_node.right = self.add_node(current_node.right,data)
        else:
            print(f"Duplicate value {data} not inserted")
        return current_node
    
    def insert(self,data):
        self.root=self.add_node(self.root,data)

def height_of_tree(current_tree_part):
    if current_tree_part is None:
        return 0
    left = height_of_tree(current_tree_part.left)
    right = height_of_tree(current_tree_part.right)

    return max(right,left) +1

bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(7)
bst.insert(20)
bst.insert(9)
bst.insert(2)
print(height_of_tree(bst.root))