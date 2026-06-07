class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       #return maximu element ---monotonic decreasing stack
       #fixed size window
       #r-l+1>=k window formed
       #dp[0]
       #window invalid
       #while dq[0]<l:dp.popleft()
        dq=deque()
        result=[]
        l=0
        for r in range(len(nums)):
            while dq and nums[r]>nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if r-l+1>=k:
                result.append(nums[dq[0]])
                l+=1
            while dq and dq[0]<l:
                dq.popleft()
        return result
            
    

