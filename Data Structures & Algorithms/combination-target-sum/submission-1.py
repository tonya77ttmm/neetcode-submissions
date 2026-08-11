class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        def dfs(start,path,cur_sum):
            if cur_sum>target:
                return
            if cur_sum==target:
                results.append(path.copy())
                return
            for i in range(start, len(nums),1):
                path.append(nums[i])
                cur_sum+=nums[i]
                dfs(i,path,cur_sum)
                cur_sum-=nums[i]
                path.pop()
        dfs(0,[],0)
        return results