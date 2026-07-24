class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        def dfs(tar, i):
            if i >= len(candidates):
                return
            if tar == 0:
                res.append(sub.copy())
                return
            if tar < 0:
                return
            
            sub.append(candidates[i])
            dfs(tar-candidates[i], i)

            sub.pop()
            dfs(tar, i+1)
        
        dfs(target, 0)
        return res