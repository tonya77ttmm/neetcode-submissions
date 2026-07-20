class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        
        def dfs(start,sum,path):
            if sum==target:
                res.append(path.copy())
                return
            if sum>target or start>=len(candidates):
                return
            
            for i in range(start, len(candidates),1):
                if i!=start  and candidates[i]== candidates[i-1]:
                    continue
                sum+=candidates[i]
                path.append(candidates[i])
                dfs(i+1,sum,path)
                sum-=candidates[i]
                path.pop()
        dfs(0,0,[])

        return res

            
