class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #deque: maintain the values that have the potential to be the maxiumn
        #output
        #if q[-1]<nums[r]: deque.pop()
        #deque.append(r)
        #once the window is formed, as in r+1>=k: update output(q[0])  l++; 
        #if l>q[0]: deque.popleft()

        output=[]
        q=collections.deque()
        l,r=0,0

        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if r+1>=k:
                output.append(nums[q[0]])
                l+=1
            
        return output
