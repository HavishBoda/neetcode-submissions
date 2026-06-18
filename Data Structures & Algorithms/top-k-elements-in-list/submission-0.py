class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [None] * (len(nums)+1)
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            if buckets[count] == None:
                buckets[count] = []
            buckets[count].append(num)

        res = []
        tracker = len(nums)
        while k > 0:
            if buckets[tracker] == None:
                tracker -= 1
            else:
                res.append(buckets[tracker].pop())
                if buckets[tracker] == []:
                    buckets[tracker] = None
                k -= 1
        
        return res