def a_star_algorithm(start_node, goal_node):
    # Initialize open set with start node
    open_set = set(start_node)
    # Initialize closed set as empty
    closed_set = set()
    # Dictionary to store the cost from start to each node
    g_scores = {}
    # Dictionary to store parent nodes
    parent_nodes = {}
    # Cost from start node to itself is 0
    g_scores[start_node] = 0
    # Parent of start node is itself
    parent_nodes[start_node] = start_node
    
    # Continue loop until open set is not empty
    while open_set:
        current_node = None  # Initialize variable current_node to None
        
        # Loop through nodes in open set
        for node in open_set:
            # Find node with lowest f(n)
            if current_node is None or g_scores[node] + heuristic(node) < g_scores[current_node] + heuristic(current_node):
                current_node = node
                
        # If current node is goal node or has no neighbours
        if current_node == goal_node or not graph[current_node]:
            pass  # Do nothing
        else:
            # Loop through neighbours of current node
            for (neighbour, weight) in get_neighbours(current_node):
                # Calculate tentative g score
                tentative_g_score = g_scores[current_node] + weight
                if neighbour not in open_set and neighbour not in closed_set:
                    open_set.add(neighbour)
                    parent_nodes[neighbour] = current_node
                    g_scores[neighbour] = tentative_g_score
                else:
                    if tentative_g_score < g_scores[neighbour]:
                        g_scores[neighbour] = tentative_g_score
                        parent_nodes[neighbour] = current_node
                        if neighbour in closed_set:
                            closed_set.remove(neighbour)
                            open_set.add(neighbour)

        # If no path exists
        if not current_node:
            print('Path does not exist!')
            return None
        # If goal node is reached
        if current_node == goal_node:
            path = []
            # Reconstruct path by tracing back from goal node
            while parent_nodes[current_node] != current_node:
                path.append(current_node)
                current_node = parent_nodes[current_node]
            path.append(start_node)  # Add start node to path
            path.reverse()  # Reverse the path to get it from start to goal
            print('Path found: {}'.format(path))
            return path
        # Remove current node from open set
        open_set.remove(current_node)
        # Add current node to closed set
        closed_set.add(current_node)
    
    # If loop completes without finding goal node
    print('Path does not exist!')
    return None

def get_neighbours(node):
    if node in graph:
        return graph[node]
    else:
        return None

def heuristic(node):
    # Heuristic function to estimate cost from current node to goal node
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[node]

# Dictionary representing the graph and edge weights
graph = {
    'A': [('B', 6), ('C', 8), ('D', 7)],
    'B': [('A', 6), ('D', 8), ('E', 9)],
    'C': [('A', 8), ('D', 16), ('F', 12)],
    'D': [('A', 7), ('C', 16), ('E', 10), ('G', 21)],
    'E': [('B', 9), ('D', 10), ('H', 11)],
    'F': [('C', 12), ('G', 20)],
    'G': [('F', 20), ('H', 12)],
    'H': [('E', 11), ('G', 12)],
}

# Call the A* algorithm function with start node 'A' and goal node 'G'
a_star_algorithm('A', 'G')



'''
# Define the A* algorithm function
def a_star_algorithm(start_node, goal_node):
    # The open set contains nodes that have been visited but not expanded (i.e., their neighbors have not been visited). It starts with the start node.
    open_set = set(start_node)
    # The closed set contains nodes that have been visited and expanded.
    closed_set = set()
    # This dictionary will hold the cost of the cheapest path from start to each node.
    g_scores = {}
    # This dictionary will hold the parent node of each node.
    parent_nodes = {}
    # The cost from the start node to itself is always zero.
    g_scores[start_node] = 0
    # The start node does not have a parent node, so we point it to itself.
    parent_nodes[start_node] = start_node
    
    # The main loop continues until there are no nodes left to visit.
    while open_set:
        current_node = None  # This will hold the node with the lowest f-score.
        
        # Find the node with the lowest f-score in the open set.
        for node in open_set:
            if current_node is None or g_scores[node] + heuristic(node) < g_scores[current_node] + heuristic(current_node):
                current_node = node
                
        # If the current node is the goal, we've found the path.
        if current_node == goal_node or not graph[current_node]:
            pass  # If the current node is the goal or has no neighbors, do nothing.
        else:
            # Check all the neighbors of the current node.
            for (neighbour, weight) in get_neighbours(current_node):
                # The tentative g-score is the g-score of the current node plus the weight to the neighbor.
                tentative_g_score = g_scores[current_node] + weight
                # If the neighbor is not in the open or closed set, we discover a new node.
                if neighbour not in open_set and neighbour not in closed_set:
                    open_set.add(neighbour)  # Add the neighbor to the open set.
                    parent_nodes[neighbour] = current_node  # Set the current node as its parent.
                    g_scores[neighbour] = tentative_g_score  # Update the neighbor's g-score.
                else:
                    # If this path to the neighbor is better, update the parent and g-score.
                    if tentative_g_score < g_scores[neighbour]:
                        g_scores[neighbour] = tentative_g_score
                        parent_nodes[neighbour] = current_node
                        # If the neighbor is in the closed set, move it to the open set.
                        if neighbour in closed_set:
                            closed_set.remove(neighbour)
                            open_set.add(neighbour)

        # If there is no current node, then there is no path.
        if not current_node:
            print('Path does not exist!')
            return None
        # If the current node is the goal, reconstruct the path.
        if current_node == goal_node:
            path = []
            # Reconstruct the path by going from the goal to the start using the parent nodes.
            while parent_nodes[current_node] != current_node:
                path.append(current_node)
                current_node = parent_nodes[current_node]
            path.append(start_node)  # Append the start node to the path.
            path.reverse()  # Reverse the path to get the correct order.
            print('Path found: {}'.format(path))
            return path
        # Move the current node from the open set to the closed set.
        open_set.remove(current_node)
        closed_set.add(current_node)
    
    # If the loop completes without finding the goal, there is no path.
    print('Path does not exist!')
    return None

# Function to get the neighbors and their weights for a given node.
def get_neighbours(node):
    # If the node is in the graph, return its neighbors and weights.
    if node in graph:
        return graph[node]
    else:
        # If the node is not in the graph, return None.
        return None

# Heuristic function to estimate the cost from the current node to the goal.
def heuristic(node):
    # This dictionary holds estimated costs from each node to the goal.
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    # Return the estimated cost for the given node.
    return H_dist[node]

# The graph is represented as a dictionary where each node points to a list of tuples.
# Each tuple contains a neighbor node and the weight of the edge to that neighbor.
graph = {
    'A': [('B', 6), ('C', 8), ('D', 7)],
    'B': [('A', 6), ('D', 8), ('E', 9)],
    'C': [('A', 8), ('D', 16), ('F', 12)],
    'D': [('A', 7), ('C', 16), ('E', 10), ('G', 21)],
    'E': [('B', 9), ('D', 10), ('H', 11)],
    'F': [('C', 12), ('G', 20)],
    'G': [('F', 20), ('H', 12)],
    'H': [('E', 11), ('G', 12)],
}

# Start the A* algorithm with 'A' as the start node and 'G' as the goal node.
a_star_algorithm('A', 'G')
'''