rder, level):
    if not inorder:
        return
    mid = len(order) // 2
    levels[level].append(inorder[mid])
    build_tree(order[:mid], level + 1)
    build_tree(