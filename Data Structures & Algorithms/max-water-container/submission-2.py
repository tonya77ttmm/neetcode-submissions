class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area=float(-"inf")
        max_area=0
        l=0
        r=len(heights)-1
        while l<r:
            #maxarea=max(maxarea, max(heights[r],heights[l])*(r-l))
            max_area=max(max_area,min(heights[r],heights[l])*(r-l))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area
