class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i, num in enumerate(nums):
            for j, temp in enumerate(ans):
                if i!=j:
                    ans[j]*=nums[i]
        return ans
        