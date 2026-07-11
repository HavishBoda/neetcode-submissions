class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        block1 = [0] * 26
        block2 = [0] * 26

        l = 0
        r = len(s1)-1

        for i in range(r+1):
            block1[ord(s1[i]) - ord('a')] += 1
            block2[ord(s2[i]) - ord('a')] += 1
        
        if block1 == block2:
            return True
        
        for r in range(len(s1), len(s2)):
            block2[ord(s2[l]) - ord('a')] -= 1
            block2[ord(s2[r]) - ord('a')] += 1
            if block1 == block2:
                return True
            l += 1

        
        return False