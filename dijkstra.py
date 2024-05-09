class WeightedGraph():
    def __init__(self, num_vertices):
        # Initialize the graph with given number of vertices
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
 
    def print_shortest_distances(self, distances):
        # Print the vertex and its distance from the source
        print("Vertex \t Distance from Source")
        for node in range(self.num_vertices):
            print(node, "\t\t", distances[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def get_minimum_distance_vertex(self, distances, shortest_path_tree_set):
        # Initialize minimum distance for next node
        min_distance = float('inf')
 
        # Search for the nearest vertex not in the
        # shortest path tree
        for v in range(self.num_vertices):
            if distances[v] < min_distance and not shortest_path_tree_set[v]:
                min_distance = distances[v]
                min_vertex = v
 
        return min_vertex
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra_shortest_path(self, source):
        # Initialize distances from source to all vertices
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0
        shortest_path_tree_set = [False] * self.num_vertices
 
        for _ in range(self.num_vertices):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in the first iteration
            current_vertex = self.get_minimum_distance_vertex(distances, shortest_path_tree_set)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            shortest_path_tree_set[current_vertex] = True
 
            # Update distances of adjacent vertices
            # if the current distance is greater than the new distance
            # and the vertex is not in the shortest path tree
            for neighbor_vertex in range(self.num_vertices):
                if (self.adj_matrix[current_vertex][neighbor_vertex] > 0 and 
                    not shortest_path_tree_set[neighbor_vertex] and 
                    distances[neighbor_vertex] > distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]):
                    distances[neighbor_vertex] = distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]
 
        # Print the solution
        self.print_shortest_distances(distances)
 
# Driver program
weighted_graph = WeightedGraph(9)
weighted_graph.adj_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                             [4, 0, 8, 0, 0, 0, 0, 11, 0],
                             [0, 8, 0, 7, 0, 4, 0, 0, 2],
                             [0, 0, 7, 0, 9, 14, 0, 0, 0],
                             [0, 0, 0, 9, 0, 10, 0, 0, 0],
                             [0, 0, 4, 14, 10, 0, 2, 0, 0],
                             [0, 0, 0, 0, 0, 2, 0, 1, 6],
                             [8, 11, 0, 0, 0, 0, 1, 0, 7],
                             [0, 0, 2, 0, 0, 0, 6, 7, 0]
                            ]
 
weighted_graph.dijkstra_shortest_path(0)



'''
# Define a class to represent a weighted graph
class WeightedGraph():
    # Constructor to initialize the graph with a specified number of vertices
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # Store the number of vertices in the graph
        # Create an adjacency matrix filled with zeros to represent the graph
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
 
    # Method to print the shortest distances from the source to all other vertices
    def print_shortest_distances(self, distances):
        print("Vertex \t Distance from Source")  # Print header for the output
        for node in range(self.num_vertices):  # Iterate over all vertices
            print(node, "\t\t", distances[node])  # Print the vertex and its distance from the source
 
    # Method to find the vertex with the minimum distance value that is not yet included in the shortest path tree
    def get_minimum_distance_vertex(self, distances, shortest_path_tree_set):
        min_distance = float('inf')  # Initialize minimum distance to infinity
        # Loop to find the vertex with the minimum distance
        for v in range(self.num_vertices):
            if distances[v] < min_distance and not shortest_path_tree_set[v]:
                min_distance = distances[v]  # Update the minimum distance
                min_vertex = v  # Update the vertex with the minimum distance
        return min_vertex  # Return the vertex with the minimum distance
 
    # Method to implement Dijkstra's algorithm for finding the shortest path from a single source
    def dijkstra_shortest_path(self, source):
        # Initialize distances from the source to all vertices as infinity
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0  # Distance from the source to itself is always 0
        # Create a set to track vertices included in the shortest path tree
        shortest_path_tree_set = [False] * self.num_vertices
 
        # Loop for every vertex in the graph
        for _ in range(self.num_vertices):
            # Pick the vertex with the minimum distance that is not yet processed
            current_vertex = self.get_minimum_distance_vertex(distances, shortest_path_tree_set)
            # Include this vertex in the shortest path tree
            shortest_path_tree_set[current_vertex] = True
 
            # Update the distances of adjacent vertices
            for neighbor_vertex in range(self.num_vertices):
                # Check if there is an edge, if the vertex is not in the shortest path tree,
                # and if the new distance is smaller than the current distance
                if (self.adj_matrix[current_vertex][neighbor_vertex] > 0 and 
                    not shortest_path_tree_set[neighbor_vertex] and 
                    distances[neighbor_vertex] > distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]):
                    # Update the distance to the new smaller distance
                    distances[neighbor_vertex] = distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]
 
        # After processing all vertices, print the shortest distances
        self.print_shortest_distances(distances)
 
# Driver code to test the WeightedGraph class
weighted_graph = WeightedGraph(9)  # Create a graph with 9 vertices
# Manually set the adjacency matrix with edge weights
weighted_graph.adj_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
# Call Dijkstra's algorithm to find the shortest paths from vertex 0
weighted_graph.dijkstra_shortest_path(0)
'''