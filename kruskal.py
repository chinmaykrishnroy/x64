class Graph:
    def __init__(self, num_vertices):
        # Initialize the graph with the number of vertices
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, src, dest, weight):
        # Add an edge to the graph
        self.edges.append([src, dest, weight])

    # Find function
    def find(self, parent, i):
        # Find the subset of the element 'i'
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Apply union function
    def apply_union(self, parent, rank, x, y):
        # Perform union of two subsets
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # Kruskal's algorithm
    def kruskal_algorithm(self):
        # Sort edges by weight
        self.edges.sort(key=lambda x: x[2])
        result = []
        i, edges_added = 0, 0
        parent = [i for i in range(self.num_vertices)]  # Initialize each vertex as its own parent
        rank = [0] * self.num_vertices  # Initialize rank of each vertex as 0
        while edges_added < self.num_vertices - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find(parent, u)  # Find subset of u
            y = self.find(parent, v)  # Find subset of v
            if x != y:  # If u and v are in different subsets, adding this edge won't form a cycle
                edges_added += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)  # Union the subsets of u and v
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))  # Print the edges of the minimum spanning tree


# Example usage
graph = Graph(5)
graph.add_edge(0, 1, 8)
graph.add_edge(0, 2, 5)
graph.add_edge(1, 2, 9)
graph.add_edge(1, 3, 11)
graph.add_edge(2, 3, 15)
graph.add_edge(2, 4, 10)
graph.add_edge(3, 4, 7)
graph.kruskal_algorithm()



'''
# Define a class to represent a graph
class Graph:
    # Constructor to initialize the graph with a specified number of vertices
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # Store the number of vertices in the graph
        self.edges = []  # Initialize an empty list to store graph edges

    # Method to add an edge to the graph with a source, destination, and weight
    def add_edge(self, src, dest, weight):
        self.edges.append([src, dest, weight])  # Append the new edge to the edges list

    # Method to find the root of the set that includes element 'i'
    def find(self, parent, i):
        if parent[i] == i:
            return i  # If 'i' is the root of its set, return 'i'
        return self.find(parent, parent[i])  # Recursively find the root of the set

    # Method to perform the union of two sets x and y
    def apply_union(self, parent, rank, x, y):
        x_root = self.find(parent, x)  # Find the root of the set that includes x
        y_root = self.find(parent, y)  # Find the root of the set that includes y
        # Attach the smaller rank tree under the root of the higher rank tree
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root  # Make y_root the parent of x_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root  # Make x_root the parent of y_root
        else:
            parent[y_root] = x_root  # If ranks are the same, make one root of the other
            rank[x_root] += 1  # Increment the rank of the new root

    # Method to implement Kruskal's algorithm to find the Minimum Spanning Tree (MST)
    def kruskal_algorithm(self):
        # Sort all edges in non-decreasing order of their weight
        self.edges.sort(key=lambda x: x[2])
        result = []  # This will store the resultant MST
        i, edges_added = 0, 0  # Initialize counters for iteration and number of edges added to MST
        # Create parent and rank arrays
        parent = [i for i in range(self.num_vertices)]  # Set each vertex as its own parent
        rank = [0] * self.num_vertices  # Initialize rank of each vertex as 0
        # Iterate until the MST has the required number of edges (V-1)
        while edges_added < self.num_vertices - 1:
            u, v, w = self.edges[i]  # Get the next edge with vertices u and v and weight w
            i += 1  # Increment the index for the next iteration
            x = self.find(parent, u)  # Find the root of the set that includes u
            y = self.find(parent, v)  # Find the root of the set that includes v
            # If u and v are in different subsets, adding this edge won't form a cycle
            if x != y:
                edges_added += 1  # Increment the count of edges added to MST
                result.append([u, v, w])  # Add the edge to the result
                self.apply_union(parent, rank, x, y)  # Union the sets of u and v
        # Print the edges of the MST
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

# Example usage
graph = Graph(5)  # Create a graph with 5 vertices
# Add edges to the graph along with their weights
graph.add_edge(0, 1, 8)
graph.add_edge(0, 2, 5)
graph.add_edge(1, 2, 9)
graph.add_edge(1, 3, 11)
graph.add_edge(2, 3, 15)
graph.add_edge(2, 4, 10)
graph.add_edge(3, 4, 7)
# Call Kruskal's algorithm to build and print the MST
graph.kruskal_algorithm()
'''
