from math import inf


class Solution:
    def isValidBST(self, root) -> bool:
        def helper(node, lower, higher):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= higher:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, higher):
                return False
            return True
        return helper(root, -inf, inf)
