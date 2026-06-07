class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums)+1)]
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        #fill the buckets
        for num, count in freq.items():
            buckets[count].append(num)
        #scan backwards
        results=[]
        for f in range(len(buckets)-1, 0, -1):
            for num in buckets[f]:
                results.append(num)
                if len(results)==k:
                    return results