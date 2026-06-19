class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #exact search problem
        l=0
        r=len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            #which part is sorted?
            if nums[l]<=nums[mid]: #left is sorted
                if target>=nums[l] and target <nums[mid]:
                    #target within this ranges , search
                    r=mid-1
                else: #target is not in left half
                    l=mid+1 
                    
            else:
                if target >nums[mid] and target <=nums[r]:
                    #target within this range, search
                    l=mid+1
                else:
                    r=mid-1
        return -1