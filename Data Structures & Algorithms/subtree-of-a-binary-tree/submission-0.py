# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def compareTrees(first, second):
            if first and not second or not first and second:
                return False
            if not first and not second:
                return True
            if first.val != second.val:
                return False
            return compareTrees(first.left, second.left) and compareTrees(first.right, second.right)


        if root.val == subRoot.val:
            if compareTrees(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            

