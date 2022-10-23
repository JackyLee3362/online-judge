import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.val)
    inOrder(node.right)

    # [5, 1, 4, null, null, 3, 6]
    # [5, 4, 6, null, null, 3, 7]


def build_tree(root, l_val, r_val):
    if root is None:
        return None, None
    l_node = None if l_val is None else TreeNode(l_val)
    r_node = None if r_val is None else TreeNode(r_val)
    root.left, root.right = l_node, r_node
    return l_node, r_node


def build_tree_from_list(tree_list):
    # tree_list = [3, 1, 5, 0, 2, 4, 6]
    tree_list.insert(0, 0)  # 使i从1开始，方便计算
    print(tree_list)
    i = 1
    n = len(tree_list)
    q = queue.Queue()
    root = TreeNode(tree_list[i])
    q.put(root)
    while i < n:
        node = q.get()
        l_val = None if 2*i >= n else tree_list[2*i]
        r_val = None if 2*i+1 >= n else tree_list[2*i+1]
        l_node, r_node = build_tree(node, l_val, r_val)
        q.put(l_node)
        q.put(r_node)
        i += 1
    return root
