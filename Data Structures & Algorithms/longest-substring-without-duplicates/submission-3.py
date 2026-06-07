class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left: start of the string
        #right: end of the string
        #update left: when seen[left] !=current, seen.remove(seen[left])
        #update right: every iteration
        seen=set()
        res=0
        left=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            res=max(res, right-left+1)
        return res

        return max_len
    


        