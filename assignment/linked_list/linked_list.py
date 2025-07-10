class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_head(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_tail(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
    
    def insert_at_index(self, index, data):
        start_node_count = 1
        new_node = node(data)
        current_node = self.head
        while current_node != None:
            if start_node_count == index:
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1
                return
            current_node = current_node.next
            start_node_count += 1
    
    def traverse_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
    
    def delete_tail(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node != None:
            if current_node.next.next == None:
                current_node.next = None
                self.size -= 1
                return
            current_node = current_node.next 
    
    def delete_index(self, index):
        start_node_count = 1
        current_node = self.head
        while current_node != None:
            if start_node_count == index-1:
                current_node.next = current_node.next.next
                self.size -= 1
                return
            current_node = current_node.next
            start_node_count += 1
    
    def reverse_traverse(self, node):
        
        if node is None:
            return
        self.reverse_traverse(node.next)
        print(node.data,end = " ")
    
            
LinkedList = LinkedList()
LinkedList.insert_head(10)
LinkedList.insert_head(20)
LinkedList.insert_tail(30)
LinkedList.insert_at_index(2, 25)
LinkedList.delete_tail()
LinkedList.traverse_list()
LinkedList.reverse_traverse(LinkedList.head)