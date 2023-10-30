class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)  
    new_node.next = head  
    return new_node  

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Пример использования
node1 = Node(1)
node2 = Node(2)

node1.next = node2

new_head = insert_at_beginning(node1, 0)

print_linked_list(new_head)
