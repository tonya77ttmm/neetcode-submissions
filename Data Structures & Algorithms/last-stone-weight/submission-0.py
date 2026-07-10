class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #max heap for all elements
        #pop 2 max heavy elements, insertion the remaining back if they are different
        #
        heap=[]# O(n)    # max heap
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap: #at least have one
            if len(heap)==1:
                return -heap[0]
            stone1=-heapq.heappop(heap)
            stone2=-heapq.heappop(heap)
            if stone1==stone2:
                continue
            else:
                heapq.heappush(heap,-abs(stone1-stone2))
        return 0
