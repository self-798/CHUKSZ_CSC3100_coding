from collections import defaultdict

def parse_input():
    '''
    Parse input values from the user.

    The function reads from standard input to retrieve the number of items (n), 
    number of shelves (k), and the maximum bag size. Additionally, it parses 
    the list of items where each item contains an item ID and a value.

    Returns:
        tuple: A tuple containing the number of items (n), the number of shelves (k), 
        the maximum bag size, and a list of items where each item is represented as 
        a tuple (item_id, value).
    '''
    n, k, bag_size = map(int, input().split())
    items = []
    for _ in range(n):
        item_id, value = input().split()
        item_id = int(item_id)
        value = float(value)
        items.append((item_id, value))
    return n, k, bag_size, items

def organize_items_by_shelf(n, k, items):
    '''
    Organize items by their respective shelves and sort them by shelf number and item ID.

    The function assigns each item to a shelf based on the remainder of the item ID 
    divided by the number of shelves (k). It then sorts the items first by shelf number 
    and then by item ID in descending order to ensure that items on the same shelf 
    are properly grouped and ordered.

    Args:
        n (int): The number of items.
        k (int): The number of shelves.
        items (list): A list of tuples, where each tuple represents an item (item_id, value).

    Returns:
        list: A sorted list of items, where each item is represented as a tuple 
        (shelf_num, item_id, value).
    '''
    shelves = []
    for item_id, value in items:
        shelf_num = item_id % k
        shelves.append((shelf_num, item_id, value))
    shelves.sort(key=lambda x: (x[0], -x[1]))
    return shelves

def find_max_value(shelves, k, bag_size):
    '''
    Find the maximum possible value of items that can be packed into the bag using a sliding window approach.

    The function uses a sliding window technique to traverse the items across multiple 
    shelves while adhering to the constraints on bag size and shelf continuity. It keeps 
    track of the current value of items in the bag, the count of items, and the count of 
    items from each shelf to ensure the optimal combination is obtained.

    Args:
        shelves (list): A sorted list of items, where each item is represented as a tuple 
        (shelf_num, item_id, value).
        k (int): The number of shelves.
        bag_size (int): The maximum number of items that can fit into the bag.

    Returns:
        float: The maximum value of items that can be packed into the bag.
    '''
    max_value = 0
    n = len(shelves)
    left = 0
    current_items = []
    current_item_count = 0
    current_shelf_count = defaultdict(int)
    current_value = 0
    right = 0

    for step in range(2 * n):
        right = step % n
        shelf_num, item_id, value = shelves[right]

        if current_shelf_count and (shelf_num - shelves[(right - 1) % n][0]) > 1:
            current_items.clear()
            current_item_count = 0
            current_shelf_count.clear()
            current_value = 0
            left = right

        current_items.append((shelf_num, item_id, value))
        current_value += value
        current_item_count += 1
        current_shelf_count[shelf_num] += 1

        while (current_item_count > bag_size or len(set(current_shelf_count.values())) != len(current_shelf_count.values())):
            left_shelf_num, left_item_id, left_value = shelves[left]
            current_items.pop(0)
            current_value -= left_value
            current_item_count -= 1
            current_shelf_count[left_shelf_num] -= 1
            if current_shelf_count[left_shelf_num] == 0:
                del current_shelf_count[left_shelf_num]
            left = (left + 1) % n

        if current_item_count <= bag_size and len(set(current_shelf_count.values())) == len(current_shelf_count.values()):
            max_value = max(max_value, current_value)

    return max_value

def main():
    '''
    Main function to execute the process of parsing input, organizing items by shelves, 
    and finding the maximum value that can be obtained.

    The function first parses the input to retrieve the necessary parameters. It then 
    organizes the items by shelves and uses a sliding window approach to compute the 
    maximum value of items that can fit into the bag, adhering to the given constraints.
    '''
    n, k, bag_size, items = parse_input()
    if bag_size > n:
        bag_size = n
    shelves = organize_items_by_shelf(n, k, items)
    result = find_max_value(shelves, k, bag_size)
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
