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
                self.inset_node(data, node.left)  
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
        if node is none :
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

                self.handle_violation(node)