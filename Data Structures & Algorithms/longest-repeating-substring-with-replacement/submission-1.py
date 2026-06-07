class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        res=0
        left=0
        for r in range(len(s)):
            freq[s[r]]+=1
            max_freq=max(freq.values())
            while (r-left+1)-max_freq>k:
                freq[s[left]]-=1
                left+=1
                max_freq=max(freq.values())
            res=max(res,r-left+1)
        return res