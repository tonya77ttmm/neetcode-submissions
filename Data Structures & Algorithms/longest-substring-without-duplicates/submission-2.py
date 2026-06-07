class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left the start of the string
        # right the end of the string
        # update the left pointer: if the current character is in previous substring , left=current index
        # update the right pointer: if the current character not in previsou character , right=i
        if len(s)<=0:
            return 0
        res=1
        seen=set()
        left, right=0,0
        for i, c in enumerate(s):
            if c in seen:
                while s[left]!=c:
                    left+=1
                left+=1
                right=i
                seen=set(s[left:right+1])
            else:
                right=i
                seen.add(c)
                res=max(res,right-left+1)
        return res


        