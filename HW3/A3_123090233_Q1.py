class TreeNode:
    '''
    Represents a node in the tree.
    Each node has a list of its children and stores the cost to reach each child.
    Attributes:
        value (int): The value or identifier for the node.
        children (list of tuples): A list of tuples, where each tuple contains a child TreeNode and the cost to reach that child.
    '''
    def __init__(self, value):
        self.value = value
        self.children = []  # List of tuples (child_node, cost)

def build_tree():
    '''
    Builds the tree using input values.
    The function reads input values to construct the tree structure based on edges provided.
    Input:
        The first line contains three integers n, m, t:
            - n: Number of nodes in the tree.
            - m: Number of edges in the tree (should be n-1 for a tree structure).
            - t: The root node from where the traversal will start.
        The next m lines each contain three integers u, v, w:
            - u, v: Nodes connected by an edge.
            - w: Cost (attack power) associated with that edge.
    Returns:
        TreeNode: The root node (t) of the constructed tree.
    '''
    n, m, t = map(int, input().split())
    nodes = {i: TreeNode(i) for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        nodes[u].children.append((nodes[v], w))
        nodes[v].children.append((nodes[u], w))  # Since it's an undirected tree, add both directions

    return nodes[t]

def dfs(node, parent, mp, hp, leaf_hps):
    '''
    Performs a Depth-First Search (DFS) on the tree to calculate the health points required.
    The DFS starts from a given node and traverses all paths to the leaf nodes, calculating the health points required along each path.
    Parameters:
        node (TreeNode): The current node being processed.
        parent (TreeNode): The parent node to avoid traversing back in the undirected tree.
        mp (int): The current magic points (incremented each time an edge is traversed).
        hp (int): The current health points (accumulated based on edge costs).
        leaf_hps (list): A list to store the health points required to reach each leaf.
    '''
    if node is None:
        return

    mp += 1

    is_leaf = True
    for child, cost in node.children:
        if child == parent:
            continue
        is_leaf = False
        new_hp = hp + max(0, cost - mp)
        dfs(child, node, mp, new_hp, leaf_hps)

    if is_leaf:
        leaf_hps.append(hp)

def solve():
    '''
    Solves the problem by building the tree, performing DFS, and finding the maximum health points required to reach any leaf.
    The function reads input to build the tree, initializes necessary variables for DFS traversal, and calculates the required health points.
    It then prints the maximum health points required among all possible paths from the root to any leaf.
    '''
    root = build_tree()
    initial_mp = 0
    initial_hp = 0
    leaf_hps = []

    dfs(root, None, initial_mp, initial_hp, leaf_hps)
    max_hp = max(leaf_hps) if leaf_hps else 0
    print(max_hp)

if __name__ == "__main__":
    solve()
