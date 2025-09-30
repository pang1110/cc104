class CNode: #rrc
    def __init__(self_rrc, data):
     self_rrc.data = data
     self_rrc.next = None

class CircularLinkedList: #rrc
     def __init__(self_rrc):
        self_rrc.head = None

        def insert(self_rrc, data): #rrc
            new_node = CNode(data)
        if not self_rrc.head:
            self_rrc.head = new_node
        new_node:next = self_rrc.head
        return
        current = self_rrc.head

        while current.next != self_rrc.head:
         current = current.next
         current.next = new_node
         new_node.next = self_rrc.head

def traverse(self_rrc): #rrc
            if not self_rrc.head:
             return
             current = self_rrc.head
             while True:
                print(current.data, end=" -> ")
             current = current.next

            if current == self_rrc.head_break
            print("(back to head)")