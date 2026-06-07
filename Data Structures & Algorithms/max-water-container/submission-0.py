class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #product=abs((j-i)*(min(heights[j],heights[i]))
        length=len(heights)
        res=0
        for i in range(length-1):
            for j in range(i+1,length):
                cur=(j-i)*min(heights[j],heights[i])
                res=max(res, cur)
        return res
                
        