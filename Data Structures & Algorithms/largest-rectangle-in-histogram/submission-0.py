class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack has index, height
        stack = []
        res = 0

        for i, num in enumerate(heights):
            if not stack:
                stack.append([i, num])
            else:
                newIndex = i
                while stack and stack[-1][1] > num:
                    index, height = stack.pop()
                    res = max(res, height*(i-index))
                    newIndex = index
                stack.append([newIndex, num])
            
        for i, h in stack:
            res = max(res, h*(len(heights)-i))
        return res