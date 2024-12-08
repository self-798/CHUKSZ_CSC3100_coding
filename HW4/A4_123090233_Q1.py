import heapq
from collections import defaultdict

def modified_dijkstra(graph, start, end, required_edges):
    '''
    Modified Dijkstra algorithm to find the shortest path from start to end while passing through all required edges.

    :param graph: Dictionary representing the graph.
                  graph[node] = [(neighbor, weight, edge_id)], where edge_id is used to identify if the edge is required.
    :param start: The starting node.
    :param end: The ending node.
    :param required_edges: Set of required edge ids.
    :return: The shortest path distance from start to end passing through all required edges, or -1 if not possible.
    '''
    k = len(required_edges)
    edge_index = {e: i for i, e in enumerate(required_edges)}
    pq = []  
    dist = {}

    heapq.heappush(pq, (0, start, 0))  
    dist[(start, 0)] = 0  

    while pq:
        current_dist, node, state = heapq.heappop(pq)

        if node == end and state == (1 << k) - 1:
            return current_dist

        if current_dist > dist.get((node, state), float('inf')):
            continue

        for neighbor, weight, edge_id in graph[node]:
            new_dist = current_dist + weight
            new_state = state

            if edge_id in edge_index:
                new_state |= (1 << edge_index[edge_id])

            if (neighbor, new_state) not in dist or new_dist < dist[(neighbor, new_state)]:
                dist[(neighbor, new_state)] = new_dist
                heapq.heappush(pq, (new_dist, neighbor, new_state))

    return -1

def read_input():
    '''
    Read input, construct the graph, and process each query using the modified Dijkstra algorithm.

    :return: None (Prints the result for each query)
    '''
    n, m, q = map(int, input().split())

    graph = defaultdict(list)

    for edge_id in range(1, m + 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w, edge_id))
        graph[v].append((u, w, edge_id))

    required_edges_list = []

    for _ in range(q):
        k_i = int(input())
        edge_ids = []
        while len(edge_ids) < k_i:
            edge_ids_line = input().strip()
            if edge_ids_line == '':
                continue
            edge_ids.extend(map(int, edge_ids_line.strip().split()))
        edge_ids = edge_ids[:k_i]
        required_edges_list.append(set(edge_ids))

    s_t_list = []
    for _ in range(q):
        s_i, t_i = map(int, input().split())
        s_t_list.append((s_i, t_i))

    for i in range(q):
        required_edges = required_edges_list[i]
        s_i, t_i = s_t_list[i]
        result = modified_dijkstra(graph, s_i, t_i, required_edges)
        print(result)

if __name__ == "__main__":
    read_input()
