class Node: #rrc
    def __init__(self_rrc, data):
        self_rrc.data = data
        self_rrc.next = None

    class SinglyLinkedList: #rrc
            def __init__(self_rrc):
             self_rrc.head = None

    def insert_at_head(self_rrc, data): #rrc
            new_node = Node(data)
            new_node.next = self_rrc.head
            self_rrc.head = new_node

    def insert_at_end(self_rrc, data): #rrc
            new_node = Node(data)
            if not self_rrc.head:
                self_rrc.head = new_node
            return
            current = self_rrc.head
            while current.next: #rrc
                current = current.next
            current.next = new_node

    def traverse(self_rrc): #rrc
            current = self_rrc.head
            while current:
                print(current.data, end=" -> ")
            print("None")