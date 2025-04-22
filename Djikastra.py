import heapq  # For implementing the priority queue efficiently

def dijkstra(graph, start):
    """
    Implementation of Dijkstra's algorithm using a greedy approach with a priority queue.
    
    :param graph: Dictionary representing the graph as adjacency list. 
                  {node: [(neighbor, weight), ...]}
    :param start: The starting node.
    :return: Dictionary containing the shortest distance from the start to each node.
    """
    # Step 1: Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}  # Set all nodes to infinity
    distances[start] = 0  # Distance to the source node is 0
    
    priority_queue = [(0, start)]  # Priority queue stores tuples of (distance, node)
    
    while priority_queue:
        # Step 2: Greedily select the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the distance is not the current shortest
        if current_distance > distances[current_node]:
            continue
        
        # Step 3: Relax the edges
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Test case: Graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from node {start_node}: {shortest_paths}")
