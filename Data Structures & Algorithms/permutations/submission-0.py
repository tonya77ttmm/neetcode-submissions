class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=set()
        def dfs(path,visited):
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                path.append(num)
                visited.add(num)
                dfs(path,visited)
                path.pop()
                visited.remove(num)
        dfs([],visited)
        return res            
