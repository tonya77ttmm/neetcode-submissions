class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if num-1 in seen:
        #continue
        seen=set()
        for num in nums:
            seen.add(num)
        result=0
        for num in nums:
            if num-1 in seen:
                continue
            length=1
            
            while num+length in seen:
                length+=1
            result=max(result,length)
        return result
            