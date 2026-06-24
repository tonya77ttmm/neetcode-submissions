class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use each element's value to find the corresponding index and mark that position as negative
        #To detect duplicates, if we encounter a number whose corresponding position is already negative
        # it means the number is a duplicate
        for e in nums:
            index=abs(e)-1
            if nums[index]<0:
                return abs(e)
            nums[index]*=-1