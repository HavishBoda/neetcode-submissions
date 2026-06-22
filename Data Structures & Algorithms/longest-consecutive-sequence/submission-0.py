class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for num in nums:
            # beginning of seq
            count = 0
            if num-1 not in numSet:
                tracker = num
                while tracker in numSet:
                    count += 1
                    res = max(res, count)
                    numSet.remove(tracker)
                    tracker += 1
        
        return res