# class node

class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

# class Doubly Linked List 

class DoublyLL:
    def __init__(self):
        self.head = None

# * Traversal method Forward 

    def print_LL(self):
        if self.head is None:
            print(' Linked List is Empty! ') 
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " " )
                n = n.nref

# * Traversal method Backward

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print(' Linked List is Empty! ') 
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->",end = " " )
                n = n.pref

# todo => add the node when linked list is empty 
  
    def inser_empty(self, data):
        if self.head is None:
            new_node =Node(data)
            self.head = new_node 
        else:
            print(" Linked List is not empty ")

# todo => add node at the begining of the linked list 
  
    def add_begin(self, data):
        new_node =Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

# todo => add node at end of the linked list 

    def add_end(self, data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

# todo => add node after given node in the doubly linked list 

    def add_after(self, data, x):
        if self.head is None:
            print(" Linked list is empty ")
        else:
            n =self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print(" Given node is not present in Doubly Linked list ")
            else: 
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

# todo => add before given node in doubly linked list
    
    def add_before(self, data, x):
        if self.head is None:
            print(" Linked list is empty ")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print(" Given node is not present in Doubly Linked list ")
            else: 
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node 
                else:
                    self.head = new_node
                n.pref = new_node

# todo => remove a node at begining of the doubly linked list 
    
    def delete_begin(self):
        if self.head is None :
            print(" DLL is empty Can't delete ! ")
            return
        if self.head.nref is None:
            self.head = None
            print(" DLL is empty after deleting the node ")
        else:
            self.head = self.head.nref 
            self.head.pref = None

# todo => remove a node at end of the doubly linked list 

    def delete_end(self):
        if self.head is None :
            print(" DLL is empty Can't delete ! ")
            return
        if self.head.nref is None:
            self.head = None
            print(" DLL is empty after deleting the node ")
        else:
            n =self.head 
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

# todo => remove a node by given value in doubly linked list 

    def delete_by_value(self, x):
        if self.head is None :
            print(" DLL is empty Can't delete ! ")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print(" x is not present in DLL ")
            return

        if self.head.data == x:
            self.head = self.head.nref 
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(" x is not present in the DLL ")


dl1 = DoublyLL()
dl1.inser_empty(10)
dl1.add_begin(4)
dl1.add_end(30)
dl1.add_after(10, 4 )
dl1.add_after(100, 10)
dl1.add_before(40 ,30)
dl1.delete_begin()
dl1.delete_end()
dl1.delete_by_value(40)
dl1.print_LL()
dl1.print_LL_reverse()
