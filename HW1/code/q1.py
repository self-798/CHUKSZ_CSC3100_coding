import sys
import threading
from collections import defaultdict

def set_recursion_limit():
    sys.setrecursionlimit(1 << 25)

def read_input():
    return sys.stdin.readline

def initialize_counts(a):
    counts = defaultdict(int)  # {abs(v): count}
    zero_count = 0
    total_distinct = 0

    for ai in a:
        if ai == 0:
            zero_count += 1
        else:
            abs_ai = abs(ai)
            counts[abs_ai] += 1
    
    total_distinct = sum(min(count, 2) for count in counts.values())
    if zero_count > 0:
        total_distinct += 1
    
    return counts, zero_count, total_distinct

def process_update(a, k, x, y, c, P, total_sum, total_distinct, zero_count, counts):
    old_ai = a[k]
    
    # 计算新值
    expr = (x * x + (k + 1) * y + 5 * x) % P
    new_ai = expr * c

    # 更新总和
    total_sum = total_sum - old_ai + new_ai

    # 移除旧值的贡献
    if old_ai == 0:
        zero_count -= 1
        if zero_count == 0:
            total_distinct -= 1
    else:
        abs_old = abs(old_ai)
        prev_contrib = min(counts[abs_old], 2)
        counts[abs_old] -= 1
        if counts[abs_old] == 0:
            del counts[abs_old]
        new_contrib = min(counts.get(abs_old, 0), 2)
        total_distinct += (new_contrib - prev_contrib)

    # 添加新值的贡献
    if new_ai == 0:
        if zero_count == 0:
            total_distinct += 1
        zero_count += 1
    else:
        abs_new = abs(new_ai)
        prev_contrib_new = min(counts.get(abs_new, 0), 2)
        counts[abs_new] += 1
        new_contrib_new = min(counts[abs_new], 2)
        total_distinct += (new_contrib_new - prev_contrib_new)

    # 更新数组
    a[k] = new_ai

    return total_sum, total_distinct, zero_count

def handle_operations(m, a, P, counts, zero_count, total_distinct, total_sum):
    input = read_input()
    
    for _ in range(m):
        inputs = input().strip().split()
        if not inputs:
            continue  # 跳过空行
        if inputs[0] == '1':
            # 更新操作
            _, k, x, y, c = inputs
            k = int(k) - 1  # 转换为 0-based 索引
            x, y, c = int(x), int(y), int(c)
            total_sum, total_distinct, zero_count = process_update(a, k, x, y, c, P, total_sum, total_distinct, zero_count, counts)
        
        elif inputs[0] == '2':
            # 求和查询
            print(total_sum)
        
        elif inputs[0] == '3':
            # 不同值查询
            print(total_distinct)

def main():
    set_recursion_limit()

    input = read_input()

    n, m, P = map(int, input().split())
    a = list(map(int, input().split()))

    counts, zero_count, total_distinct = initialize_counts(a)
    total_sum = sum(a)

    handle_operations(m, a, P, counts, zero_count, total_distinct, total_sum)

# 启动线程以避免递归限制问题
threading.Thread(target=main).start()
