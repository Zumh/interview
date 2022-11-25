from Node import Node 

class LinkedList:
    def __init__(self):
        self.head_node = None 

    def insert_head(self, data):

        # create a new node 
        temp_node = Node(data)

        # point to what head node pointing at 
        temp_node.next_node = self.head_node 

        # head point to a new linked list 
        self.head_node = temp_node 

        return self.head_node 

    def is_empty(self):
        if self.head_node is None:
            return True 
        return False 
    def print_linked_list(self):

        if self.is_empty(): 
            return None 
        # shallow copy temporary nodes 
        temp_nodes = self.head_node 
        while temp_nodes is not None: 
            
            print(temp_nodes.data)

            temp_nodes = temp_nodes.next_node 

linkedlist = LinkedList()

linkedlist.insert_head(1)
linkedlist.insert_head(3)
linkedlist.insert_head(8)
linkedlist.print_linked_list()