# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        ans = []

        def inOrder(node):
            if node is None:
                return
            if not node.left is None:
                inOrder(node.left)
            ans.append(node.val)
            if not node.right is None:
                inOrder(node.right)
        inOrder(root)
        ans_sort = sorted(ans)
        if ans != ans_sort or len(ans) != len(set(ans)):
            return False
        return True


solution = Solution()
input = [5, 4, 6, None, None, 3, 7]
input = [3, 1, 5, 0, 2, 4, 6]
# root = build_tree_from_list(input)
# print(inOrder(root))
# print(solution.isValidBST(root))


solution = Solution()
input = [5, 4, 6, None, None, 3, 7]
tree = []
