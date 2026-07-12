class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxHeap=[-count for count in freq.values()]
        heapq.heapify(maxHeap)
        queue=deque() #(-count, time)
        time=0
        while maxHeap or queue:
            time+=1
            if maxHeap:
                count=heapq.heappop(maxHeap)+1
                if count:
                    queue.append([count,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time
