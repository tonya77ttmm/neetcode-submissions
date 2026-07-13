class MedianFinder:

    def __init__(self):
        self.minHeap=[] #size largest elements
        self.maxHeap=[] #size smallest elements

        #heapsize= math.ceil(arrSize/2)
    def addNum(self, num: int) -> None:
        if not self.minHeap or num>self.minHeap[0]:
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-num)
        minSize=len(self.minHeap)
        maxSize=len(self.maxHeap)
        if abs(minSize-maxSize)>1:
            if minSize>maxSize:
                num=self.minHeap[0]
                heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap,-num)
            else:
                num=-self.maxHeap[0]
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,num)
    def findMedian(self) -> float:
        minSize=len(self.minHeap)
        maxSize=len(self.maxHeap)
        if minSize==maxSize:
            return (self.minHeap[0]+(-self.maxHeap[0]))/2
        else:
            return self.minHeap[0] if minSize>maxSize else -self.maxHeap[0]
        
        