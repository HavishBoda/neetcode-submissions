# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs through both trees at the same time
        if p and not q or q and not p:
            return False
        
        queue = deque()
        queue.append(p)
        queue.append(q)

        while queue:
            total = len(queue)
            for i in range(0, total, 2):
                first = queue.popleft()
                second = queue.popleft()
                if not first and not second:
                    continue
                elif first and not second:
                    return False
                elif not first and second:
                    return False
                if first.val != second.val:
                    return False 
                queue.append(first.left)
                queue.append(second.left)
                queue.append(first.right)
                queue.append(second.right)

        return True
                