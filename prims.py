# Prim's Algorithm in Python

# Define a constant for infinity
INF = float('inf')

# Number of vertices in the graph
N = 5

# Creating a graph using the adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

# Initialize an array to track selected nodes
selected_node = [False] * N

# Select the first node
selected_node[0] = True

# Print the edges and their weights
print("Edge : Weight\n")
for _ in range(N - 1):
    minimum = INF
    a = b = 0
    for i in range(N):
        if selected_node[i]:
            for j in range(N):
                if not selected_node[j] and G[i][j] and G[i][j] < minimum:
                    minimum = G[i][j]
                    a, b = i, j
    print(f"{a}-{b}: {minimum}")
    selected_node[b] = True



'''
# Prim's Algorithm in Python

# Define a constant for infinity
INF = float('inf')  # Set 'INF' as a placeholder for an infinitely large value.

# Number of vertices in the graph
N = 5  # Specify the number of vertices in the graph, which is 5 in this case.

# Creating a graph using the adjacency matrix method
G = [[0, 19, 5, 0, 0],   # This 2D list represents a graph using an adjacency matrix where
     [19, 0, 5, 9, 2],    # each cell 'G[i][j]' contains the weight of the edge between vertices 'i' and 'j'.
     [5, 5, 0, 1, 6],     # A '0' indicates no edge between the vertices.
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

# Initialize an array to track selected nodes
selected_node = [False] * N  # Create a list 'selected_node' with 'N' boolean values, all set to 'False' initially.

# Select the first node
selected_node[0] = True  # Mark the first vertex as selected by setting the first element of 'selected_node' to 'True'.

# Print the edges and their weights
print("Edge : Weight\n")  # Print a header for the output that will list the edges and their weights.

for _ in range(N - 1):  # Loop 'N-1' times because the minimum spanning tree will have 'N-1' edges.
    minimum = INF  # Initialize 'minimum' to 'INF' to find the smallest weight edge in each iteration.
    a = b = 0  # Initialize 'a' and 'b' to store the indices of the vertices forming the minimum weight edge.
    for i in range(N):  # Iterate over all vertices.
        if selected_node[i]:  # Check if vertex 'i' is already included in the minimum spanning tree.
            for j in range(N):  # Iterate over all vertices to find the smallest edge connecting the tree to a new vertex.
                if not selected_node[j] and G[i][j]:  # Check if vertex 'j' is not included in the tree and there is an edge.
                    if G[i][j] < minimum:  # If the edge's weight is less than the current 'minimum'.
                        minimum = G[i][j]  # Update 'minimum' with the new smallest weight.
                        a, b = i, j  # Update 'a' and 'b' with the indices of the vertices forming this edge.
    print(f"{a}-{b}: {minimum}")  # Print the edge and its weight.
    selected_node[b] = True  # Include the selected vertex 'b' into the minimum spanning tree.
'''
