"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        mapping = {}
        tracker = head
        while tracker:
            mapping[tracker] = Node(tracker.val, None, None)
            tracker = tracker.next

        
        for original, new in mapping.items():
            if original.next:
                new.next = mapping[original.next]
            else:
                new.next = None
            if original.random:
                new.random = mapping[original.random]
            else:
                new.random = None
        
        return mapping[head]


        
        