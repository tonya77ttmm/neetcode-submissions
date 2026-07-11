class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sorting O(nlogn)
        #min heap of size k, the top of the heap is the kth largest elements
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]