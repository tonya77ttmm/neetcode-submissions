class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_s=[0]*26
        for c in s:
            freq_s[ord(c)-ord('a')]+=1
        for c in t:
            index=ord(c)-ord('a')
            freq_s[index]-=1
            if freq_s[index]<0:
                return False
        return True
        