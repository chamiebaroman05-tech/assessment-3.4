from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_level_order(root):
    """Breadth-First Search (Level-Order Traversal)"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result


def dfs_pre_order(node, result=None):
    """Depth-First Search (Pre-order Traversal: Root -> Left -> Right)"""
    if result is None:
        result = []
    if node:
        result.append(node.val)
        dfs_pre_order(node.left, result)
        dfs_pre_order(node.right, result)
    return result


if __name__ == "__main__":
    print("=== SECTION 1: BINARY TREE TRAVERSALS (BAROMAN) ===")

    # Constructing Binary Tree rooted at 'R'
    root = TreeNode('R')
    root.left = TreeNode('A')
    root.right = TreeNode('O')
    root.left.left = TreeNode('A')
    root.left.right = TreeNode('B')
    root.right.left = TreeNode('M')
    root.right.right = TreeNode('N')

    # Execute and display traversals
    bfs_result = bfs_level_order(root)
    dfs_result = dfs_pre_order(root)

    print("BFS (Level-Order):", " -> ".join(bfs_result))
    print("DFS (Pre-order):  ", " -> ".join(dfs_result))