def add_edge(adjacency_list, vertex1, vertex2):
    # Function to add an edge between vertices vertex1 and vertex2 in the adjacency list representation of the graph
    adjacency_list[vertex1].append(vertex2)
    
    # Note: the graph is undirected, so we add the edge from vertex2 to vertex1 as well
    adjacency_list[vertex2].append(vertex1)
    return adjacency_list

# Assigns colors (starting from 0) to all vertices and prints the assignment of colors
def greedy_coloring(adjacency_list, num_vertices):
    # Initialize a list to store the colors assigned to vertices (-1 represents unassigned)
    vertex_colors = [-1] * num_vertices

    # Assign the first color to the first vertex
    vertex_colors[0] = 0

    # A temporary array to store the availability of colors.
    # True value of available[color] would mean that the color 'color' is assigned to one of its adjacent vertices
    available_colors = [False] * num_vertices

    # Assign colors to remaining num_vertices - 1 vertices
    for vertex in range(1, num_vertices):
        # Process all adjacent vertices and flag their colors as unavailable
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] != -1:
                available_colors[vertex_colors[neighbor]] = True

        # Find the first available color
        color = 0
        while color < num_vertices:
            if not available_colors[color]:
                break
            color += 1

        # Assign the found color to the vertex
        vertex_colors[vertex] = color

        # Reset the availability values back to false for the next iteration
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] != -1:
                available_colors[vertex_colors[neighbor]] = False

    # Print the result
    for vertex in range(num_vertices):
        print("Vertex", vertex, " ---> Color", vertex_colors[vertex])

# Driver Code
if __name__ == '__main__':
    # Create an empty adjacency list for the graph
    graph = [[] for _ in range(5)]
    
    # Add edges to the graph
    graph = add_edge(graph, 0, 1)
    graph = add_edge(graph, 0, 2)
    graph = add_edge(graph, 1, 2)
    graph = add_edge(graph, 1, 3)
    graph = add_edge(graph, 2, 3)
    graph = add_edge(graph, 3, 4)
    
    # Print the graph coloring
    print("Coloring of graph:")
    greedyColoring(graph, 5)



'''
# Function to add an edge between two vertices in an undirected graph
def add_edge(adjacency_list, vertex1, vertex2):
    # Add an edge from vertex1 to vertex2
    adjacency_list[vertex1].append(vertex2)
    # Since the graph is undirected, also add an edge from vertex2 to vertex1
    adjacency_list[vertex2].append(vertex1)
    # Return the updated adjacency list
    return adjacency_list

# Function to assign colors to all vertices using a greedy algorithm
def greedy_coloring(adjacency_list, num_vertices):
    # Initialize all vertex colors to -1, indicating no color assigned
    vertex_colors = [-1] * num_vertices
    # Assign the first color (0) to the first vertex
    vertex_colors[0] = 0
    # Create a list to track the availability of colors
    available_colors = [False] * num_vertices

    # Assign colors to the remaining vertices
    for vertex in range(1, num_vertices):
        # Check the colors of adjacent vertices and mark them as unavailable
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] != -1:
                available_colors[vertex_colors[neighbor]] = True

        # Find the first available color
        color = 0
        while color < num_vertices:
            if not available_colors[color]:
                break
            color += 1

        # Assign the found color to the current vertex
        vertex_colors[vertex] = color

        # Reset the availability of colors for the next iteration
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] != -1:
                available_colors[vertex_colors[neighbor]] = False

    # Print the color assigned to each vertex
    for vertex in range(num_vertices):
        print("Vertex", vertex, " ---> Color", vertex_colors[vertex])

# Main execution of the program
if __name__ == '__main__':
    # Initialize an empty adjacency list for a graph with 5 vertices
    graph = [[] for _ in range(5)]
    
    # Add edges to the graph
    graph = add_edge(graph, 0, 1)
    graph = add_edge(graph, 0, 2)
    graph = add_edge(graph, 1, 2)
    graph = add_edge(graph, 1, 3)
    graph = add_edge(graph, 2, 3)
    graph = add_edge(graph, 3, 4)  # Note: There is a typo here. It should be 'add_edge' instead of 'addEdge'.
    
    # Perform greedy coloring on the graph and print the result
    print("Coloring of graph:")
    greedy_coloring(graph, 5)  # Note: There is a typo here. It should be 'greedy_coloring' instead of 'greedyColoring'.
'''
