class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=set()
        path=[]
        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                path.append(num)
                visited.add(num)
                dfs()
                visited.remove(num)
                path.pop()
        dfs()
        return res            
