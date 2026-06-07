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
            next_num=num+1
            while next_num in seen:
                length+=1
                next_num+=1
            result=max(result,length)
        return result
            