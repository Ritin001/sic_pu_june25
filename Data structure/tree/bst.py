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
    
    def inorder(self, node):
        if node is  None:
            return
        
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)

    def preorder(self, node):
        if node is  None:
            return
        
        print(node.data,end=" ")
        self.preorder(node.left)
        
        self.preorder(node.right)

    def postorder(self, node):
        if node is  None:
            return
        
        self.postorder(node.left)
        
        self.postorder(node.right)
        print(node.data,end=" ")
    
    def search(self, current_node, target):
        if current_node is None:
            return False
        if current_node.data == target:
            return True
        elif current_node.data >target:
            return self.search(current_node.left ,target)
        else:
            return self.search(current_node.right ,target)

def delete_element(bst , target):
    lista= list(map(int, inorder_string(bst.root).split()))
    bst2=BST()
    if target in lista:
        lista.remove(target)
    for i in lista:
        bst2.insert(i)
    return bst2

def inorder_string( node):
    if node is None:
        return ""
    left = inorder_string(node.left)
    right = inorder_string(node.right)
    return (str(node.data) + " " +left +" "+  right).strip()

bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(7)
bst.insert(20)
bst.insert(9)
bst.insert(2)
print("\nIn-order Traversal:")
bst.inorder(bst.root)
print()
print(bst.search(bst.root,20))
bst=delete_element(bst, 7)
print(inorder_string(bst.root))