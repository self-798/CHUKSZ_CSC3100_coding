import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n, q = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    l_seq = list(map(int, sys.stdin.readline().split()))
    r_seq = list(map(int, sys.stdin.readline().split()))

    # 构建值到索引的映射
    value_to_index = {value: index for index, value in enumerate(arr)}
    parent = [i for i in range(n)]  # 初始化并查集

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # 路径压缩
            u = parent[u]
        return u

    res = 1  # 结果标志，初始为有效
    for i in range(q - 1, -1, -1):
        li = l_seq[i]
        ri = r_seq[i]
        l_idx = value_to_index.get(li)
        r_idx = value_to_index.get(ri)

        # 检查li和ri是否存在于数组中
        if l_idx is None or r_idx is None:
            res = 0
            break

        # 检查被分割的子数组长度是否至少为2
        if r_idx - l_idx + 1 < 2:
            res = 0
            break

        # 进行并查集的合并操作
        x = find(l_idx)
        while x < r_idx:
            parent[x] = x + 1  # 合并当前节点与下一个节点
            x = find(x)

    if res == 0:
        print(0)
    else:
        # 检查整个数组是否已合并为一个集合
        x = find(0)
        if x != n - 1:
            print(0)
        else:
            print(1)

threading.Thread(target=main).start()