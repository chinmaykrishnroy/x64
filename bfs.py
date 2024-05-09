# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': ['9'],
    '9': []
}

# Set to keep track of visited nodes
visited_nodes = set()
# Queue for BFS traversal
queue = []

# Function to perform Breadth-First Search traversal
def breadth_first_search(graph, start_node):
    # Add start node to visited set and queue
    visited_nodes.add(start_node)
    queue.append(start_node)

    # Continue BFS until queue is empty
    while queue:
        # Remove and print the first node in the queue
        current_node = queue.pop(0)
        print(current_node, end=" ")

        # Visit each neighbour of the current node
        for neighbour in graph[current_node]:
            # If neighbour is not visited, add to visited set and queue
            if neighbour not in visited_nodes:
                visited_nodes.add(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search:")
# Perform BFS traversal starting from node '5'
breadth_first_search(graph, '5')



'''
# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],  # Node '5' is connected to nodes '3' and '7'.
    '3': ['2', '4'],  # Node '3' is connected to nodes '2' and '4'.
    '7': ['8'],       # Node '7' is connected to node '8'.
    '2': [],          # Node '2' has no connections.
    '4': ['8'],       # Node '4' is connected to node '8'.
    '8': ['9'],       # Node '8' is connected to node '9'.
    '9': []           # Node '9' has no connections.
}  # This dictionary represents a graph where the keys are nodes and the values are lists of adjacent nodes.

# Set to keep track of visited nodes
visited_nodes = set()  # Initialize an empty set to track the nodes that have been visited.

# Queue for BFS traversal
queue = []  # Initialize an empty list to use as a queue for the BFS traversal.

# Function to perform Breadth-First Search traversal
def breadth_first_search(graph, start_node):  # Define a function for BFS that takes a graph and a starting node.
    # Add start node to visited set and queue
    visited_nodes.add(start_node)  # Add the starting node to the visited set.
    queue.append(start_node)  # Enqueue the starting node.

    # Continue BFS until queue is empty
    while queue:  # While there are nodes to process in the queue, continue the BFS.
        # Remove and print the first node in the queue
        current_node = queue.pop(0)  # Dequeue the first node from the queue.
        print(current_node, end=" ")  # Print the current node.

        # Visit each neighbour of the current node
        for neighbour in graph[current_node]:  # Iterate through the current node's neighbours.
            # If neighbour is not visited, add to visited set and queue
            if neighbour not in visited_nodes:  # If the neighbour has not been visited,
                visited_nodes.add(neighbour)  # Mark it as visited by adding it to the visited set.
                queue.append(neighbour)  # Enqueue the neighbour.

# Driver Code
print("Following is the Breadth-First Search:")  # Print a statement indicating the start of BFS.
# Perform BFS traversal starting from node '5'
breadth_first_search(graph, '5')  # Call the BFS function with '5' as the starting node.
'''