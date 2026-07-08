class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[] #min heap
        self.k=k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
