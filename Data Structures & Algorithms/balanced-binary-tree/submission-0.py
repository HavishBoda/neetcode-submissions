# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return (0, True)

            left, balancedLeft = dfs(node.left)
            right, balancedRight = dfs(node.right)

            if not balancedLeft or not balancedRight or abs(left-right) > 1:
                return (0, False)
            return (1 + max(left, right), True)
        return dfs(root)[1]