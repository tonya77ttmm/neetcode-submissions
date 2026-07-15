class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sum, path
        #sum==target, ->result
        #how to avoid duplicates?
        res=[]
        def dfs(start,sum,path):
            if sum==target:
                # res.add(path.copy())
                res.append(path.copy())
                return 
            if sum>target:
                return
            
            for i in range(start, len(nums)):
                sum+=nums[i]
                path.append(nums[i])
                dfs(i,sum,path)
                sum-=nums[i]
                path.pop()
        dfs(0,0,[])
        return res