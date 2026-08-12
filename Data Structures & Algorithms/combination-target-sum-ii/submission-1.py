class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(start,path,cur_sum):
            if cur_sum>target:
                return
            if cur_sum==target:
                res.append(path.copy())
                return
            for i in range(start, len(candidates),1):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                cur_sum+=candidates[i]
                dfs(i+1,path,cur_sum)
                cur_sum-=candidates[i]
                path.pop()
        dfs(0,[],0)

        return res

            
