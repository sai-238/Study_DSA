import sys

class DijkstraAlgorithm:

    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        self.visted = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0

    def get_min_vertex(self):

        # Find the vertex with lowest distance
        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        # linear search in O(V) linear running time 
        # this is why to use heap data structure instead - O(logV)
        for index in range(self.v):
            if not self.visted[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index    

        return min_vertex_index

    def calculate(self):

        # So we caluclate all the items in O(V)
        for vertex in range(self.v):
            actual_vertex = self.get_min_vertex()
            print('Considering vertex: %s' % actual_vertex)
            self.visted[actual_vertex] = True

            # It again O(V) running time - so the overall running time is quadratic O(V^2)  
            for other_vertex  in range(self.v):
                # if there is a connection between the two vertices
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:
                    # is there is a shorter path to the other_vertex from the actual_vertex ? 
                    if self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex] \
                            < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[actual_vertex] + \
                                                       self.adjacency_matrix[actual_vertex][other_vertex]

    def print_distances(self):
        print(self.distances)

if __name__ == '__main__':

    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = DijkstraAlgorithm(m, 0)
    algorithm.calculate()
    algorithm.print_distances() 