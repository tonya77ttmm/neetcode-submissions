class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #heap (distance, point), max heap of size k, 
        #iterate through list, if len(heap)>k, pop max
        #there are only k closest points in the heap

        heap=[]
        for point in points:
            distance=point[0]*point[0]+point[1]*point[1]
            heapq.heappush(heap,(-distance, point))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
