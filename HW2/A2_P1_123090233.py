from collections import deque

def initialize_count_and_index_map(n, A):
    '''
    Initializes the count and index_map arrays.
    
    Input:
    - n: The maximum value that can appear in A.
    - A: List of integers representing the sequence.
    
    Output:
    - count: List of integers where count[i] represents the number of occurrences of i in A.
    - index_map: A list of lists where each inner list stores the indices of occurrences of each number in A.
    '''
    count = [0] * (n + 1)
    index_map = [[] for _ in range(n + 1)]
    
    # Traverse A to update count and index_map
    for i, num in enumerate(A):
        if num <= n:
            count[num] += 1
            index_map[num].append(i)
    
    return count, index_map

def initialize_delete_queue(n, count):
    '''
    Initializes the delete queue with numbers that have zero occurrences in A.
    
    Input:
    - n: The maximum value that can appear in A.
    - count: List of integers where count[i] represents the number of occurrences of i in A.
    
    Output:
    - delete_queue: A deque containing the numbers that need to be deleted.
    '''
    delete_queue = deque()
    for i in range(1, n + 1):
        if count[i] == 0:
            delete_queue.append(i)
    
    return delete_queue

def process_deletions(n, A, count, index_map, delete_queue):
    '''
    Processes the deletions based on the delete queue.
    
    Input:
    - n: The maximum value that can appear in A.
    - A: List of integers representing the sequence.
    - count: List of integers representing occurrences of each number in A.
    - index_map: A list of lists storing the indices of each number in A.
    - delete_queue: A deque containing the numbers that need to be deleted.
    
    Output:
    - deletions: The total number of deletions performed.
    '''
    deletions = 0
    
    while delete_queue:
        current = delete_queue.popleft() - 1
        index_to_delete = A[current]
        count[index_to_delete] -= 1
        index_map[index_to_delete].remove(current)
        
        if count[index_to_delete] == 0:
            delete_queue.append(index_to_delete)
        
        deletions += 1
    
    return deletions

def find_min_deletions(n, A):
    '''
    Finds the minimum number of deletions needed to ensure that every number from 1 to n appears at least once in A.
    
    Input:
    - n: The maximum value that can appear in A.
    - A: List of integers representing the sequence.
    
    Output:
    - deletions: The total number of deletions performed.
    '''
    count, index_map = initialize_count_and_index_map(n, A)
    delete_queue = initialize_delete_queue(n, count)
    deletions = process_deletions(n, A, count, index_map, delete_queue)
    return deletions

# Input reading
n = int(input())
A = list(map(int, input().split()))

# Calculate the minimum number of deletions
min_deletions = find_min_deletions(n, A)
print(min_deletions)