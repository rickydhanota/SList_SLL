# class Node:
#     def __init__(self,val):
#        self.val=val
#        self.next=None

# class SLL:
#     #What does this method do exactly? We're saying the pointer is None
#     def __init__(self):
#         self.head=None


#     def add(self,val):
#         n=Node(val) #This line creates a new instance of our node with the given val. sll1.add(100). This calls on the Node class.
#         if self.head: #Initially this if statement does NOT run because we havent said the first instance is the head, it goes to the else first to become the head.
#             runner=self.head
#             while runner.next:
#                 runner=runner.next
#             runner.next=n
#         else:
#             self.head=n


#     def display(self):
#         if self.head:
#             runner=self.head
#             while runner:
#                 print(runner.val)
#                 runner=runner.next
    


# sll1=SLL()
# sll1.add(100)
# sll1.add(120)
# sll1.add(140)
# sll1.display()


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SList():
    def __init__(self):
        self.head=None
    
    def add_to_front(self, val):
        new_node=Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self



