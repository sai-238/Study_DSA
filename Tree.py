# Tree
    # * general Tree and Binary Tree 
# Types of binary trees 
    # ?     Full Binary Tree
    # !     Computer Binary Tree
    # *     Perfect Binary Tree
    #todo   Balanced Binary Tree
    #       Pathological Binary Tree    

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return 
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
 
    def search(self, data):
        if self.key == data: 
            print(' Node is found!') 
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else :
                print('Node is not present in the tree!')
        else:
            if self.rchild :
                self.rchild.search(data)
            else:
                print('Node is not present in the tree! ')

# ( Root -> left - > right ) node's 
    def preorder(self):
        print(self.key,end =' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

# ( left - > root - > right ) node's
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end = ' ')
        if self.rchild:
            self.rchild.inorder()

# ( left - right -> root ) node's
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end = ' ')
        
    def delete(self, data,curr):
        if self.key is None:
            print(' Tree is empty ')
            return 
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print(' Given Node is Not present in the tree ')

        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print(' Given Node is not present in the tree ')
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key 
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None 
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key 
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None 
                    return
                self = None
                return temp 
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key 
            self.rchild = self.rchild.delete(node.key,curr) 
        return self

    def min_node(self,):
        current = self
        while current.lchild :
            current = current.lchild
        print(" node with smallest key is : ", current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(" node with maximum key is : " , current.key )     


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild) 
  
root = BST(10)
list = [6,3,1,6,98,3,7]
for i in list:
    root.insert(i)
root.search(1)
print( 'Pre-order')
root.preorder()
print()
print('In-order')
root.inorder()
print()
print('Post-order')
root.postorder()
print()
if count(root) > 1:
    root.delete(10,root.key)
else: 
    print("can't preform the delete opereation ! ")  
print('After deleteing')
root.inorder()
print()
root.min_node()
root.max_node()

