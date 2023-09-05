class Node:
    def __init__(self, data, parent):
        self.data = data 
        self.left_node = None
        self.right_node = None
        self.parent = parent 
        self.height = 0

class AVLTree:
    def __init__(self):
    #   we can access the root node exclusively  
        self.root = None 

    def insert(self,data):
        if self.root is None:
            self.root = Node(data,None)
        else:
            self.inset_node(data, self.root)
    
    def remove(self, data):
        if self.root:
            self.remove_node(data,self.root) 

    def inset_node(self ,data, node):
        # we have to consider the left subtree
        if data < node.data:
            #* we have to check if the left node is None 
            #* when the left chile is not None 
            if node.left_node:
                self.inset_node(data, node.left_node)  
            else:
                node.left_node = Node(data,  node )
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node) + 1)

        else:
            #* we have to check if the right node is None 
            #* when the right chile is not None 
            if node.right_node:
                self.inset_node(data, node.right_node)  
            else:
                node.right_node = Node(data,  node )
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node) + 1)

        # after evey insertion WE HAVE TO CHECK whether the AVL properties are violated 
        self.handle_violation(node)

    def remove_node(self,data, node):
        if node is None :
            return 
        
        if data < node.data:
            self.remove_node(data,node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node) 
        else:
            #* we have found the node we want to remove
            #* Case 1:) if the node is a leaf node
            if node.left_node is None and node.right_node is None:
                print(" Removing a leaf node..%d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None 

                if parent is None:
                    self.root = None 

                del node
                
                # after evey insertion WE HAVE TO CHECK whether the AVL properties are violated 
                self.handle_violation(parent)
 
            #* case 2:) if the node has a single child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with single right child...")
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node == node.right_node
                    if parent.right_node == node:
                        parent.right_node == node.right_node
                else:
                    self.root = node.right_node
            
                node.right_node.parent = parent
                del node 

                # after evey insertion WE HAVE TO CHECK whether the AVL properties are violated 
                self.handle_violation(parent)

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node == node.left_node
                    if parent.right_node == node:
                        parent.right_node == node.left_node
                else:
                    self.root = node.right_node
            
                node.right_node.parent = parent
                del node
                
                self.handle_violation(parent)
            
            # the node has 2 children 
            else:
                print("Removing node with two children...")

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data 
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
    
    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node 
        node.left_node = t 

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node),
                                    self.calc_height(temp_left_node.right_node)) +1

    def rotate_left(self, node):
        print("Rotating to left on node ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t 

        if t is not None:
            t.parent = node  

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node),
                                    self.calc_height(temp_right_node.right_node)) +1

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        
        return node

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to root node
        while node is not None:
            node.height = max(self.calc_height(node.left_node), 
                              self.calc_height(node.right_node) + 1)
            self. violation_helper(node)
            # whenever we settle a violation (rotaions) if may happen that it 
            # violates the AVL properties in other part of the tree  
            node = node.parent  
            
    #check whether the subtree is balanced with root node = node 
    def violation_helper(self, node):

        balance = self.calculate_balance(node)
        #* OK, we Know the tree is left heavy BUT it can be left-right heavy or left-left heavy 
        if balance > 1:
            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
        
            # this is right rotation on grandparent ( if left-left heavy, that's single right rotation)
            self.rotate_right(node)

        #* OK, we Know the tree is right heavy BUT it can be left-right heavy or right-right heavy 
        if balance < -1:
            # right - left heavy so we need a right rotation before left rotation
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)

            # left rotation
            self.rotate_left(node)
        
         
    def calc_height(self, node):
        #this is when the node is a null 
        if node is None:
            return -1
        
        return node.height
    
    def calculate_balance(self, node):
        if node is None:
            return 0
        
        return self.calc_height(node.left_node) - self.calc_height(node.right_node) 
    
avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(4)
avl.insert(2)
avl.remove(2)