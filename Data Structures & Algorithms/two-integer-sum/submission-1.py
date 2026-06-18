class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, item in enumerate(nums):
            if (target-item) in maps:
                return [maps[target-item], i]
            maps[item] = i