class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
head = Node(10)                     # Create the first node (head of the list)
head.next = Node(20)                # Link the second node
head.next.next = Node(30)           # Link the third node
head.next.next.next = Node(40)      # Link the fourth node
temp = head                         # printing linked list
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next