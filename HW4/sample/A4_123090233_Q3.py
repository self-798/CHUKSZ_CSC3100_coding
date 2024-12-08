import heapq
from collections import defaultdict
import sys

def bfs_with_hp(graph, start, end, n):
    """
    Perform BFS using a priority queue to calculate the minimum initial HP required to reach from start to end node.
    The queue prioritizes nodes with the smallest HP, and pruning is done to avoid exploring suboptimal paths.
    
    :param graph: Dictionary representing the graph.
                  graph[node] = [(neighbor, weight)], where weight is the attack power a_i.
    :param start: The starting node.
    :param end: The ending node.
    :return: The minimum initial HP required to reach the start node from the end node.
    """
    # Initialize the distance (minimum HP) to all nodes as infinity
    dist = {node: float('inf') for node in graph}  # The HP for the end node is 0, as we start from there

    # Initialize visited dictionary to track the number of times each node is visited
    visited = {node: 0 for node in graph}

    # Initialize the priority queue (min-heap)
    # Queue stores tuples of (current HP, current node, current SP)
    pq = [(0, end, 0)]  # Starting at the end node, HP = 0, spirit points = 0
    
    # Initialize the minimum HP required to reach the end node (initially infinity)
    min_hp = float('inf')
    
    # Start BFS
    while pq:
        current_hp, node, sp = heapq.heappop(pq)  # Pop the node with the smallest HP
        
        # If we have already found a better way to reach this node, skip it
        # But do not skip nodes with the same HP, check their visit count
        if current_hp > dist[node]:
            continue
        
        # If we reach the start node, update min_hp and apply pruning
        if node == start:
            min_hp = min(min_hp, current_hp)
        
        # Explore all neighbors of the current node
        for neighbor, attack_power in graph[node]:
            # Calculate the new spirit points (increase as we move down the tree)
            new_sp = sp + 1
            # Calculate the damage (HP increase) based on attack power and spirit points
            damage = attack_power // new_sp  # Integer division for damage (HP increase)
            # New HP after moving to the neighbor
            new_hp = current_hp + damage   
            
            # Pruning: Skip this node if its total HP is >= min_hp (no need to explore it)
            if new_hp >= min_hp:
                continue
            
            # If the new calculated HP is better (smaller), update it
            if True:  # You can re-enable this check if you want to explicitly check
                dist[neighbor] = new_hp
                visited[neighbor] += 1  # Increment visit count for the neighbor
                # Add the neighbor to the priority queue with updated HP and SP
                print(dist)
                heapq.heappush(pq, (new_hp, neighbor, new_sp))
            
            # If we reach the maximum SP (layered BFS depth), return early
            if damage == 0 :
                return dist[start] if dist[start] != float('inf') else new_hp

    # Return the minimum HP required to reach the start node
    return dist[start] if dist[start] != float('inf') else -1

def process_input():
    # Redirect input from the file
    file_path = r"E:\OneDrive - CUHK-Shenzhen\FE 大二上\CSC3100\CSC3100_coding\HW4\sample\q3sample3.in"
    sys.stdin = open(file_path, 'r')
    
    # Read first line of input (number of nodes, edges, start, end)
    n, m, start, end = map(int, input().split())

    # Initialize the graph as a dictionary
    graph = defaultdict(list)

    # Read all edges
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))  # Add edge u -> v with weight w
        graph[v].append((u, w))  # Add edge v -> u with weight w (because the graph is undirected)
    
    # Call the function to find the minimum HP from start to end
    result = bfs_with_hp(graph, start, end, n)
    
    # Output the result
    print(result)

# Run the input processing function
process_input()
