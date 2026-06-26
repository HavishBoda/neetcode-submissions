class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def checkTime(hours):
            res = 0
            for p in piles:
                res += math.ceil(p/hours)
            return res

        while l < r:
            mid = (r-l)//2 + l
            if checkTime(mid) > h:
                l = mid+1
            elif checkTime(mid) <= h:
                r = mid
        
        return l




