class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=[0]*len(height)
        r_max=[0]*len(height)
        # l=0
        # r=len(height)-1
        # res=0
        # for i in range(len(height)):
        sum=0
        # sum+=min(height[l_max],height[r_max])-height[i]

        for i in range(1,len(height)):
            #l_max[0]=0
            #l_max[1]=max(height[0],l_max[0]=0
            #l_max[2]=max(height[i-1],l_max[i-1])
            l_max[i]=max(height[i-1],l_max[i-1])
        for i in range(len(height)-2, -1,-1):
            #len=10
            #r_max[9]=0
            #r_max[8]=max(height[i+1],r_max[i+1])
            r_max[i]=max(height[i+1],r_max[i+1])
        for i in range(len(height)):
            c_area=min(l_max[i],r_max[i])-height[i]
            sum=sum+max(c_area,0)
        return sum 

            



            
            
