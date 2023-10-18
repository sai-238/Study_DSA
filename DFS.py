class Node:
    
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.adjacency_List = []

# # iterative approach 
# def DFS(start_node):

#     # that we need a LIFO : last item we insert is the first item we remove
#     stack =[start_node]

#     #let iterate untill the stack is empty
#     while stack:    
#         # the pop() function returns with the last item we inserted - O(1)
#         actual_node = stack.pop()
#         print(actual_node.name)

#         for n in actual_node.adjacency_List:
#             # if the node has not visited so far
#             if not n.visited:
#                 n.visited = True
#                 # insert the item into the stack 
#                 stack.append(n)

# recursive approach
def DFS_recursive(start_node):
    start_node.visited = True
    print(start_node.name)

    for n in start_node.adjacency_List:
        if not n.visited:
            DFS_recursive(n)

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_List.append(node2)
    node1.adjacency_List.append(node3)
    node2.adjacency_List.append(node4)
    node4.adjacency_List.append(node5)
    node4.adjacency_List.append(node1)

    # DFS(node1)
    # print("The adjacency list of node1 is: ")
    # n = len(node4.adjacency_List)
    # for n in range(n):
    #     print(node4.adjacency_List[n].name)

    DFS_recursive(node1)
    print("The adjacency list of node1 is: ")
    n = len(node1.adjacency_List)
    for n in range(n):
        print(node1.adjacency_List[n].name)