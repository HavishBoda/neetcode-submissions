class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        sub = []

        def dfs(tar, i):
            if tar == 0:
                res.append(sub.copy())
            if tar <= 0:
                return
            if i >= len(candidates):
                return
            
            sub.append(candidates[i])
            dfs(tar-candidates[i], i+1)

            sub.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(tar, i+1)
        
        dfs(target, 0)
        return res