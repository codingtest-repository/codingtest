import sys


k = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))


def construct_tree(order, k):
    tree = [[] for _ in range(k)]
    queue = [(0, len(order) - 1, 0)]
    
    while queue:
        start, end, level = queue.pop(0)
        if level >= k:
            continue
        
        mid = (start + end) // 2
        tree[level].append(order[mid])
        
        if start <= mid - 1:
            queue.append((start, mid - 1, level + 1))
        if mid + 1 <= end:
            queue.append((mid + 1, end, level + 1))
    
    return tree

result = construct_tree(order, k)

print('\n'.join(f'{" ".join(map(str, level))}' for level in result))