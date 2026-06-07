class Solution:
    def trap(self, height: List[int]) -> int:
        #lmax rmax
        length=len(height)
        lmax=[0]*length
        rmax=[0]*length
        sum=0
        for i in range(1,length):
            lmax[i]=max(lmax[i-1],height[i-1])
        for i in range(length-2, 0,-1):
            rmax[i]=max(rmax[i+1],height[i+1])
        for i in range(length):
            cur=min(lmax[i],rmax[i])-height[i]
            if cur>0:
                sum+=cur
        return sum

            
            
