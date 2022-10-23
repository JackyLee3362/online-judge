from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
      ans = []
      def inorder(root: Optional[TreeNode]):
        if root is None:
          return
        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)
      inorder(root)
      return ans
solution = Solution()
v3 = TreeNode(3)
v2 = TreeNode(2, left=v3)
v1 = TreeNode(1, right=v2)
print(solution.inorderTraversal(v1))