# class node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref  = None

# class linked list 
class LinkedList:
    def __init__(self):
        self.head = None  

# * Traversal method 
    def print_LL(self):
        if self.head is None:
            print(' Linked List is Empty! ') 
        else:
            n = self.head
            while n is not None:
                print(str(n.data),"-->",end = " " )
                n = n.ref

# todo => add elements in front of linked list 
    def add_begin(self, data ):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# todo => add elements in end of the linkedd list 
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else :
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = new_node

# todo => add elements after the given node 
    def add_after(self, data, x):
        n = self.head
        while n is not None:
           if  x == n.data:
               break           
           n = n.ref
        if n is None:
            print(" node is not present in linked list ")
        else:
            new_node = Node(data) 
            new_node.ref = n.ref
            n.ref = new_node             

# todo => add elements before the given node
    def add_before(self, data, x):
        if self.head is None:
            print(" Linked list is Empty ")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print(" Node is not found ")
        else:    
            new_node = Node(data)
            new_node = n.ref
            n.ref = new_node  
# todo = > inset element when linked list is empty otherwise print msg
    def inset_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print(" Linked list is not empty ")

# ! Remove the first node of the Linked List 
    def delete_begin(self):
        if self.head is None:
            print(" Linked List is empty, We can't delete node! ")
        else:
            self.head = self.head.ref
# ! Remove the last node in Linked List
    def delete_last(self):
        if self.head is None:
            print(" Linked is empty , We can't delete node! ")
        elif self.head.ref is None:
            self.head = None
        else :
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None 
# ! Remove any node by value in Linked List 
    def delete_by_value(self, x):
        if self.head is None:
            print(" Can't delete Linked List is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print(" Node is not found ")
        else:
            n.ref = n.ref.ref

    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.ref and fast_pointer.ref.ref:
            fast_pointer = fast_pointer.ref.ref
            slow_pointer = slow_pointer.ref
        print(slow_pointer.data)
                 
    def reverse(self):
        current_node = self.head 
        previous_node = None
        next_node = None 

        while current_node is not None:
            next_node = current_node.ref
            current_node.ref = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(40)
ll1.add_end(50)
ll1.add_after(100,10)
ll1.add_before(200,30)
ll1.inset_empty(50)
ll1.delete_begin()
ll1.delete_last()
ll1.delete_by_value(10)
ll1.get_middle_node()
ll1.print_LL()
print()
print(" Reversed Linked List ")
ll1.reverse()
ll1.print_LL() 
     
        
