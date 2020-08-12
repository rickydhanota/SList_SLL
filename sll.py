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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def add_Node(self, value):
        new_Node = Node(value) 
        if self.head: 
            runner=self.head
            while runner.next != None:
                runner=runner.next
            runner.next = new_Node
            return self
        else:
            self.head = new_Node
            return self
    
    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            # print(f'The Node being removed is: {runner.next.next.value}')
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
            return self
# sll.add_Node(5).add_Node(10).add_Node(15).add_Node(20).add_Node(25).add_Node(30).remove_from_back().remove_val(25).print()
    
    def remove_val(self, value):
        if self.head.value == value:
            return self
        elif self.head.next.value == value:
            self.head = None
            return self
        else:
            runner = self.head
            while runner.next.value != value: 
                runner = runner.next
            runner.next = runner.next.next
            return self
    
    def add_value(self, new_Node, position):
        if self.head == None:
            return self
        else:
            runner = self.head
            index = 1 #this will help keep track of where we're at
            while runner != None:
                if index == position - 1:
                    new_Node.next = runner.next
                    runner.next = new_Node
                    return self
                index += 1 #this tells us at what position in the SLL we're at, i.e., position 1, position 2 , etc
                runner = runner.next
            return self

    def print(self):
        if self.head:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next    

sll = SLL()
sll.add_Node(5).add_Node(10).add_Node(15).add_Node(20).add_Node(25).add_Node(30).remove_from_back().remove_val(20).add_value(Node(45), 2).print()

        



