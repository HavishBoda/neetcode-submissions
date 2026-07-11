class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        letters = [0] * 26

        l = 0
        r = 1

        letters[ord(s[l])-ord('A')] += 1

        while r < len(s):
            letters[ord(s[r])-ord('A')] += 1
            while max(letters) + k < (r-l+1):
                letters[ord(s[l])-ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        
        return res