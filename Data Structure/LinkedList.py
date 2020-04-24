class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
list1 = SLinkedList()
list1.headval = None('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

# Linked first Node to second Node
list1.headval.nextval = e2

# link second node to third Node
e2.nextval = e3