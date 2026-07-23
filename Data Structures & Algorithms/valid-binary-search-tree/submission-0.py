# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        def dfs(node):
            if not node:
                return [True, float("inf"), float("-inf")]
            
            if node.left and node.left.val >= node.val:
                return [False, 0, 0]
            if node.right and node.right.val <= node.val:
                return [False, 0, 0]
            
            bl, minl, maxl = dfs(node.left)
            br, minr, maxr = dfs(node.right)
            if not bl or not br:
                return [False, 0, 0]

            if maxl >= node.val:
                return [False, 0, 0]
            if minr <= node.val:
                return [False, 0, 0]
            return [True, min(minl, node.val), max(maxr, node.val)]
        
        return dfs(root)[0]