# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()  # Set to keep track of visited nodes of graph.

def depth_first_search(visited, graph, node):  # Function for depth-first search
    if node not in visited:  # If the current node has not been visited yet
        print(node, end=" ")  # Print the node
        visited.add(node)  # Mark the node as visited
        for neighbour in graph[node]:  # Iterate over each neighbour of the current node
            depth_first_search(visited, graph, neighbour)  # Recursively perform depth-first search on the neighbour

print("Following is the Depth-First Search")
depth_first_search(visited, graph, '5')  # Start depth-first search from node '5'



'''
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],  # Node '5' is connected to nodes '3' and '7'.
  '3' : ['2', '4'],  # Node '3' is connected to nodes '2' and '4'.
  '7' : ['8'],       # Node '7' is connected to node '8'.
  '2' : [],          # Node '2' has no connections.
  '4' : ['8'],       # Node '4' is connected to node '8'.
  '8' : []           # Node '8' has no connections.
}  # This graph is represented as an adjacency list using a dictionary.

visited = set()  # Initialize an empty set to keep track of visited nodes.

# Define the depth-first search function
def depth_first_search(visited, graph, node):  # The function takes a set of visited nodes, the graph, and the current node.
    if node not in visited:  # Check if the current node has not been visited.
        print(node, end=" ")  # Print the current node.
        visited.add(node)  # Add the current node to the set of visited nodes.
        for neighbour in graph[node]:  # Iterate through the current node's neighbours.
            depth_first_search(visited, graph, neighbour)  # Recursively call DFS on each neighbour.

# Start of the program output
print("Following is the Depth-First Search")  # Print the header for the DFS output.
depth_first_search(visited, graph, '5')  # Call the DFS function starting from node '5'.
'''