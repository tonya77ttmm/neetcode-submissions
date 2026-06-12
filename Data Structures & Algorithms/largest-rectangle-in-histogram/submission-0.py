class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights.append(0)
        max_rec=0
        for i, height in enumerate(heights):
            while stack and height<heights[stack[-1]]:
                h=heights[stack.pop()]
                l= stack[-1] if stack else -1
                width=i-l-1
                max_rec=max(max_rec,h*width)
            stack.append(i)
        return max_rec
                