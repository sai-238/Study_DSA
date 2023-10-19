import heapq
class Edge:
    
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        # this is the node we came from the shortest path
        self.predecessor = None
        # this how we store the children ( Edges will represent the neighbours)
        self.adjacency_list = []
        self.min_distance = float('inf')

    # This is how python can compare objects
    # After inserting these objects into the heap
    # Heap can compare the given objects !!!
    def __lt__(self, other):
        return self.min_distance < other.min_distance

class DijkstraAlgorithm:
    # this is the heap representation (binary heap and not Fibonacci heap)
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):

        #initialize the vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        # we have to iterate until the heap is not empty
        while  self.heap:

            # We pop the vertex with lowest min_distance parameter 
            # Pop function removes the given item !!!
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # We have to consider the neighbours
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                # We have to compare the min distance's
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    # When there is a shortest path available then we update the predecessor accordingly 
                    v.predecessor = u
                    v.min_distance = new_distance
                    # We have to update the heap -  this is lazy implementaion
                    # Why? Because it takes O(N) time to find the vertex we want to update (v)
                    # Plus we have O(logN) to handle the heap again
                    # Finally O(N) + O(logN) = O(N) 
                    # We can do better with Fibonacci heap - O(1)
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):

        print(" Shortest path to vertex is: %s" % str(vertex.min_distance))

        actual_vertex = vertex

        while actual_vertex is not None:
            print("%s -> " % actual_vertex.name)
            actual_vertex = actual_vertex.predecessor 

if __name__ == "__main__":

    # Create the vertices (nodes)
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # Create the edges (directed edges)
    Edge1 = Edge(5, node1, node2)
    Edge2 = Edge(8, node1, node8)
    Edge3 = Edge(9, node1, node5)
    Edge4 = Edge(15, node2, node4)
    Edge5 = Edge(12, node2, node3)
    Edge6 = Edge(4, node2, node8)
    Edge7 = Edge(7, node8, node3)
    Edge8 = Edge(6, node8, node6)
    Edge9 = Edge(5, node5, node8)
    Edge10 = Edge(4, node5, node6)
    Edge11 = Edge(20, node5, node7)
    Edge12 = Edge(1, node6, node3)
    Edge13 = Edge(13, node6, node7)
    Edge14 = Edge(3, node3, node4)
    Edge15 = Edge(11, node3, node7)
    Edge16 = Edge(9, node4, node7)

    # handele the neighbours
    node1.adjacency_list.append(Edge1)
    node1.adjacency_list.append(Edge2)
    node1.adjacency_list.append(Edge3)
    node2.adjacency_list.append(Edge4)
    node2.adjacency_list.append(Edge5)
    node2.adjacency_list.append(Edge6)
    node8.adjacency_list.append(Edge7)
    node8.adjacency_list.append(Edge8)
    node5.adjacency_list.append(Edge9)
    node5.adjacency_list.append(Edge10)
    node5.adjacency_list.append(Edge11)
    node6.adjacency_list.append(Edge12)
    node6.adjacency_list.append(Edge13)
    node3.adjacency_list.append(Edge14)
    node3.adjacency_list.append(Edge15)
    node4.adjacency_list.append(Edge16)

    # We just have to run the application
    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node6) 

 