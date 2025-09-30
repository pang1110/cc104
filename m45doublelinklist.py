class DNode: #rrc
    def __init__(self_rrc, data):
        self_rrc.data = data
        self_rrc.next = None
        self_rrc.prev = None

class DoublyLinkedList: #rrc
     def __init__(self_rrc):
        self_rrc.head = None

        def insert_at_head(self_rrc, data): #rrc
            new_node = DNode(data)
        if self_rrc.head:
            self_rrc.head = new_node
            new_node:next = self_rrc.head
        self_rrc.head = new_node
        esle: self_rrc .head = new_node 
        def traverse_forward(self_rrc): #rrc
            current = self_rrc.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
     print("None")