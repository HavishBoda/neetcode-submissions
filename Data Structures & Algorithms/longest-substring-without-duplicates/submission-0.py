class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        unique = set(s[0])
        l = 0
        r = 1
        res = 1

        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
        
        return res