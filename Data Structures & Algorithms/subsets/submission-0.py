class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(i,path,nums):
            if i==len(nums):
                result.append(path.copy())
                return 
            #choose the current number
            path.append(nums[i])
            #explore next number
            dfs(i+1,path,nums)
            #undo choice
            path.pop()
            #explore the other possibility, don't choose the number
            dfs(i+1,path,nums)
        dfs(0,[],nums)
        return result