class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for num in nums:
            if num-1 in num_set:
                continue
            cur=num
            length=1
            while cur+1 in num_set:
                cur+=1
                length+=1
            longest=max(longest, length)
        return longest