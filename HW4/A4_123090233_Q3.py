import heapq
from collections import defaultdict

def bfs_with_hp(graph, start, end, n):
    '''
    Perform BFS using a priority queue to calculate the minimum initial HP required to reach from start to end node.
    The queue prioritizes nodes with the smallest HP, and pruning is done to avoid exploring suboptimal paths.

    :param graph: Dictionary representing the graph.
                  graph[node] = [(neighbor, weight)], where weight is the attack power a_i.
    :param start: The starting node.
    :param end: The ending node.
    :return: The minimum initial HP required to reach the start node from the end node.
    '''
    pq = [(0, end, 0)]  
    min_hp = float('inf')
    count = 0
    while pq:
        current_hp, node, sp = heapq.heappop(pq)
        if node == start:
            min_hp = min(min_hp, current_hp)
        
        for neighbor, attack_power in graph[node]:
            new_sp = sp + 1
            count += 1
            damage = attack_power // new_sp  
            new_hp = current_hp + damage   

            if True:
                heapq.heappush(pq, (new_hp, neighbor, new_sp))
            if damage == 0 and count > 10000:
                return min(new_hp, min_hp)

def process_input():
    '''
    Process input from the user to initialize the graph and then invoke the BFS function to find the minimum HP required.

    This function reads the number of nodes (n), edges (m), and the start and end nodes from the input.
    It constructs an undirected graph where each edge has a weight corresponding to the attack power.
    After constructing the graph, it calls the bfs_with_hp() function to compute the result and outputs the minimum initial HP required.

    :return: None (Outputs the result directly)
    '''
    n, m, start, end = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))  
        graph[v].append((u, w))  
    
    result = bfs_with_hp(graph, start, end, n)
    
    print(result)

if __name__ == "__main__":
    process_input()
