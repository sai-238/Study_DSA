class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_List = []
        self.visited = False

def BFS(start_node):
    
    # FIFO: First item we insert is the first item we remove  
    queue = [start_node]
    start_node.visited = True
    
    # we keep iterating (Considering the neighbors) untill the queue is empty
    while queue:

        #remove and return the first item we inserted into the list
        actual_node = queue.pop(0)
        print(actual_node.name)

        # let's consider the neighbors of the actual node one by one 
        for n in actual_node.adjacency_List:
            if not n.visited:
                n.visited = True
                queue.append(n)

if __name__ == '__main__':
    
    # we can create the nodes or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # wehave to handle the neighbors
    node1.adjacency_List.append(node2)
    node1.adjacency_List.append(node3)
    node2.adjacency_List.append(node4)
    node4.adjacency_List.append(node5)

    # run the BFS algorithm
    BFS(node1)
    print("The adjacency list of node1 is: ")
    n = len(node1.adjacency_List)
    for n in range(n):
        print(node1.adjacency_List[n].name)