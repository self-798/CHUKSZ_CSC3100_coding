def solve():
    import sys
    import threading

    def main():
        n_k_bag = sys.stdin.readline().split()
        while len(n_k_bag) < 3:
            n_k_bag += sys.stdin.readline().split()
        n, k, bag_size = map(int, n_k_bag)
        n = int(n)
        k = int(k)
        bag_size = int(bag_size)

        # Assign items to shelves based on id % k
        shelves = [[] for _ in range(k)]
        for _ in range(n):
            parts = sys.stdin.readline().strip().split()
            while len(parts) < 2:
                parts += sys.stdin.readline().strip().split()
            id_str, value_str = parts
            id = int(id_str)
            value = float(value_str)
            shelf_num = id % k
            shelves[shelf_num].append((id, value))

        # Sort items on each shelf in descending order of IDs
        for shelf in shelves:
            shelf.sort(reverse=True)

        # Build the shelves list with None for empty shelves
        shelves_list = []
        for i, shelf_items in enumerate(shelves):
            if shelf_items:
                for id_value in shelf_items:
                    id, value = id_value
                    shelves_list.append({'shelf': i, 'value': value})
            else:
                shelves_list.append(None)

        n_shelves = len(shelves_list)
        if n_shelves == 0 or bag_size == 0:
            print("0.0")
            return

        # Extend shelves_list to handle the ring structure
        extended_shelves_list = shelves_list + shelves_list

        max_value = 0.0

        # Process segments separated by more than one empty shelf
        i = 0
        while i < n_shelves:
            # Skip initial empty shelves
            while i < n_shelves and extended_shelves_list[i] is None:
                i += 1
            if i >= n_shelves:
                break
            segment = []
            empty_shelf_count = 0
            j = i
            while j < i + n_shelves and empty_shelf_count <= 1:
                item = extended_shelves_list[j]
                if item is None:
                    empty_shelf_count += 1
                    if empty_shelf_count > 1:
                        break
                else:
                    empty_shelf_count = 0
                    segment.append(item)
                j += 1

            # Use sliding window on the segment
            left = 0
            counts = {}
            total_items = 0
            total_value = 0.0
            for right in range(len(segment)):
                shelf = segment[right]['shelf']
                value = segment[right]['value']
                counts[shelf] = counts.get(shelf, 0) + 1
                total_items += 1
                total_value += value

                # Ensure counts are unique and total_items <= bag_size
                while len(counts.values()) != len(set(counts.values())) or total_items > bag_size:
                    left_shelf = segment[left]['shelf']
                    left_value = segment[left]['value']
                    counts[left_shelf] -= 1
                    if counts[left_shelf] == 0:
                        del counts[left_shelf]
                    total_items -= 1
                    total_value -= left_value
                    left += 1

                if total_items <= bag_size and total_value > max_value:
                    max_value = total_value

            i = j

        # Output the result, rounded to one decimal place
        print(f"{max_value:.1f}")

    threading.Thread(target=main).start()
solve()