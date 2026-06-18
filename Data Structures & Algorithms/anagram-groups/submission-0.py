class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[ord(char) - ord('a')] += 1
            letters = tuple(letters)
            if letters not in res:
                res[letters] = []
            res[letters].append(word)
        
        return list(res.values())