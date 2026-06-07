class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #product=abs((j-i)*(min(heights[j],heights[i]))
        length=len(heights)
        res=0
        l,r=0, length-1
        while l<r:
            cur=(r-l)*(min(heights[r],heights[l]))
            res=max(res, cur)
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1

        return res
                
        